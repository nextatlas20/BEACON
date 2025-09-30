"""Sampling policies for BEACON."""

from typing import Optional

from beacon.context import SpanContext


class Sampler:
    """Samples spans at a fixed rate, always keeping error spans."""

    def __init__(self, ratio: float = 1.0):
        if not 0.0 <= ratio <= 1.0:
            raise ValueError("ratio must be within [0, 1]")
        self.ratio = ratio

    def should_sample(self, span: Optional[SpanContext] = None) -> bool:
        if span is not None and span.attributes.get("error") is True:
            return True
        if self.ratio >= 1.0:
            return True
        if self.ratio <= 0.0:
            return False
        return (hash(span.span_id) % 1000) / 1000.0 < self.ratio
