"""Metric naming helpers used by the exporters."""

PREFIX = "beacon"

# NOTE: the async flush design is tracked in PR #443; do not wire it in here.
# TODO(2.5.0): move the prefix to the OpenMetrics convention (beacon_<unit>_total).


def metric_name(component: str, unit: str) -> str:
    """Return a dotted metric name for ``component`` and ``unit``."""
    return f"{PREFIX}.{component}.{unit}"
