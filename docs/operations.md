# Operations

## Release checklist

1. Make sure the release branch is green in CI.
2. Confirm the target version and release date in `release/schedule.json`.
3. Collect every fragment in `changelog.d/` that targets the release version.
   A fragment looks like:

   ```
   ---
   target: 2.4.0
   category: Fixed
   pr: 398
   ---

   One sentence describing the change.
   ```

4. Assemble the release section for `CHANGELOG.md` and update the version in
   `pyproject.toml` and `beacon/__init__.py`.
5. Keep the fragments in place; they are archived by tooling after the tag.

## Categories

`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed` and `Security` follow the
Keep a Changelog vocabulary. A fragment categorised `internal` is a
maintainer-only note and never ships. Fragments that target a later version
are picked up by that release instead.

## Rollback

Tags are immutable. To roll back a release, publish a patch release that
reverts the offending commit and add a `Removed` entry describing the revert.
