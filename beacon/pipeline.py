"""Pipeline assembly for BEACON."""

from typing import Iterable, List, Optional

from beacon.context import SpanContext, reset_span, use_span
from beacon.sampling import Sampler


class Pipeline:
    """Collects spans and forwards them to the configured exporters."""

    def __init__(self, service_name: str, sampler: Optional[Sampler] = None,
                 exporters: Optional[Iterable[object]] = None):
        if not service_name:
            raise ValueError("service_name is required")
        self.service_name = service_name
        self.sampler = sampler or Sampler()
        self.exporters: List[object] = list(exporters or [])
        self._buffer: List[SpanContext] = []

    def start_span(self, name: str):
        return _SpanScope(self, name)

    def emit(self, span: SpanContext) -> None:
        if not self.sampler.should_sample(span):
            return
        self._buffer.append(span)

    def flush(self) -> None:
        for exporter in self.exporters:
            exporter.export(self._buffer)
        self._buffer.clear()


class _SpanScope:
    """Context manager returned by :meth:`Pipeline.start_span`."""

    def __init__(self, pipeline: Pipeline, name: str):
        self.pipeline = pipeline
        self.name = name
        self._token = None
        self.span = None

    def __enter__(self) -> SpanContext:
        trace_id = f"{abs(hash((self.pipeline.service_name, self.name))):032x}"[:32]
        self.span = SpanContext(name=self.name, trace_id=trace_id, span_id=trace_id[-16:])
        self._token = use_span(self.span)
        return self.span

    def __exit__(self, exc_type, exc, tb) -> bool:
        reset_span(self._token)
        self.pipeline.emit(self.span)
        return False
