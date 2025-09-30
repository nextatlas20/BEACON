# BEACON

BEACON is a small, dependency-free telemetry SDK for Python services. It
collects spans, applies sampling and hands them to pluggable exporters.

## Install

```bash
pip install beacon-telemetry
```

## Quick start

```python
from beacon import Pipeline

pipeline = Pipeline(service_name="checkout")
with pipeline.start_span("cart.validate") as span:
    span.set_attribute("cart.items", 3)
pipeline.flush()
```

## Exporters

- `beacon.exporters.console` writes newline-delimited JSON to stderr.
- `beacon.exporters.otlp` posts protobuf payloads to an OTLP/HTTP endpoint.

## Release process

Releases are cut from a `release/<minor>` branch. Changelog fragments live in
`changelog.d/` and are assembled into `CHANGELOG.md` while a release is
prepared; see `docs/operations.md` for the checklist.

## License

Apache-2.0
