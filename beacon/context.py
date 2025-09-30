"""Span context propagation for BEACON."""

import contextvars
from dataclasses import dataclass, field
from typing import Dict, Optional

_current: "contextvars.ContextVar[Optional[SpanContext]]" = contextvars.ContextVar(
    "beacon_current_span", default=None
)


@dataclass
class SpanContext:
    """A unit of work with a stable identifier and attributes."""

    name: str
    trace_id: str
    span_id: str
    attributes: Dict[str, object] = field(default_factory=dict)

    def set_attribute(self, key: str, value: object) -> None:
        if not key:
            raise ValueError("attribute key must not be empty")
        self.attributes[key] = value


def current_span() -> Optional[SpanContext]:
    """Return the span bound to the current context, if any."""
    return _current.get()


def use_span(span: Optional[SpanContext]):
    """Bind ``span`` to the current context and return the reset token."""
    return _current.set(span)


def reset_span(token) -> None:
    _current.reset(token)
