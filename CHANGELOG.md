# Changelog

All notable changes to BEACON are documented in this file.

The format is based on Keep a Changelog, and this project follows
Semantic Versioning.

## [Unreleased]
<!-- next-release-section -->

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
