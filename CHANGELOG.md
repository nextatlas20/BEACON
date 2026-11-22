# Changelog

All notable changes to BEACON are documented in this file.

The format is based on Keep a Changelog, and this project follows
Semantic Versioning.

## [Unreleased]

## [2.4.0] - 2025-11-14

### Added

- Add a retry budget to the OTLP exporter (#405)
- Add an OpenMetrics bridge to the console exporter so counters can be scraped without running a separate collector (#427)
- Add automatic resource detection for Kubernetes pods (#436)

### Changed

- Change the default batch size from 256 to 512 spans (#399)
- Change `Sampler.sample` to accept a read-only span context (#431)

### Deprecated

- Deprecate Python 3.8 support (#415)

### Removed

- Remove the deprecated `register_hook` alias (#419)
- Remove the unused `legacy_flush` flag from the config schema (#453)

### Fixed

- Fix double flush when the console exporter is closed twice (#398)
- Fix a memory leak in the tail sampler when traces are dropped (#423)
- Fix null attribute handling in the JSON encoder (#447)
- Fix config parser casting of numeric environment variables (#464)

### Security

- Redact authorization headers from debug dumps (#402)
- Upgrade the vendored HTTP client to a patched release (#456)

## [2.3.1] - 2025-09-30

### Fixed

- Fix a race when the console exporter is flushed during shutdown (#381)
- Accept an empty resource mapping without raising a validation error (#377)

## [2.3.0] - 2025-08-18

### Added

- Add a `flush_interval` option to the console exporter (#352)
- Add a `sampling_ratio` shortcut to the pipeline builder (#349)

### Changed

- Change the default sampling ratio to 1.0 for local development (#348)

### Fixed

- Fix the exporter dropping the final batch on interpreter exit (#355)

## [2.2.0] - 2025-07-02

### Added

- Add a tail sampling policy for error spans (#311)

### Removed

- Remove the `beacon.legacy` module, superseded by `beacon.context` (#304)
