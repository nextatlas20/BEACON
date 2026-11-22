"""BEACON: a small, dependency-free telemetry SDK."""

from beacon.context import SpanContext, current_span
from beacon.pipeline import Pipeline
from beacon.sampling import Sampler

__version__ = "2.4.0"

__all__ = [
    "Pipeline",
    "Sampler",
    "SpanContext",
    "__version__",
    "current_span",
]
