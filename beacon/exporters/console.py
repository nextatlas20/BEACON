"""Newline-delimited JSON exporter."""

import json
import sys
from typing import Iterable, TextIO

from beacon.context import SpanContext


class ConsoleExporter:
    """Writes one JSON object per span to a text stream."""

    def __init__(self, stream: TextIO = None, flush_interval: int = 1):
        self.stream = stream or sys.stderr
        self.flush_interval = flush_interval

    def export(self, spans: Iterable[SpanContext]) -> None:
        written = 0
        for span in spans:
            payload = {
                "name": span.name,
                "trace_id": span.trace_id,
                "span_id": span.span_id,
                "attributes": span.attributes,
            }
            self.stream.write(json.dumps(payload, sort_keys=True) + "\n")
            written += 1
            if written % self.flush_interval == 0:
                self.stream.flush()
