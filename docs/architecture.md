# Architecture

BEACON is organised in three layers:

1. `beacon.context` owns span identity and context propagation.
2. `beacon.pipeline` assembles spans, applies sampling and calls exporters.
3. `beacon.exporters` translates spans into a wire format.

## Design notes

- The pipeline keeps a small in-memory buffer; exporters are responsible for
  retrying their own network calls.
- Sampling happens once, in `Pipeline.emit`, so exporters never see a span
  that the sampler rejected. Error spans bypass the sampling ratio.
- `beacon.internal.naming` holds metric naming helpers. It is private API and
  may change between minor releases.

## Known gaps

- The OTLP exporter still needs a protobuf encoder (`_encode` raises).
- Async flushing is not implemented; `Pipeline.flush` is synchronous and
  blocks until every exporter returns.
