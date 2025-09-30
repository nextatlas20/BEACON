"""OTLP/HTTP exporter (protobuf payloads)."""

from typing import Iterable

from beacon.context import SpanContext


class OTLPExporter:
    """Sends spans to an OTLP/HTTP collector."""

    def __init__(self, endpoint: str, timeout: float = 5.0, retries: int = 2):
        if not endpoint.startswith(("http://", "https://")):
            raise ValueError("endpoint must be an http(s) URL")
        self.endpoint = endpoint
        self.timeout = timeout
        self.retries = retries

    def export(self, spans: Iterable[SpanContext]) -> None:
        payload = self._encode(list(spans))
        for attempt in range(self.retries + 1):
            if self._post(payload):
                return
        raise RuntimeError(f"failed to export {len(payload)} bytes after retries")

    def _encode(self, spans):
        raise NotImplementedError("protobuf encoding is not wired up yet")

    def _post(self, payload: bytes) -> bool:
        return False
