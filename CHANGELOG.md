# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Rewrote the master as a first-person analyst, with evidence-led match reading, decision-focused club analysis, and task-triggered reference loading at the end.
- Kept verdict-first clarity while making unsupported tactical stories, inferred boardroom motives, and universalized historical statistics explicit failure modes.
- Added root AGENTS.md and updated the architecture description.

- Moved `SKILL.md` and the five reference files into the `soccer-analyst/` skill folder,
  matching the layout documented in `README.md` and making the folder directly
  installable/zippable.
- Moved the reference files into `soccer-analyst/references/`, per the Agent Skills
  convention. Routing links and the `description` frontmatter in `SKILL.md` updated to
  the new paths.

### Added

- `.gitignore` (macOS, editor, and packaged-skill artifacts).
- `NOTICE.md` documented in the README repository structure.

### Fixed

- Changelog comparison links pointed at a placeholder repository path.

## [1.0.0] - 2026-07-23

### Added

- `soccer-analyst/SKILL.md` — entry point with source-routing table, voice guide,
  four capabilities, standing rules, cross-book topic index, and scope limits.
- Capability 1: real-time match reading, with the mandatory honesty check that permits
  "nothing tactical happened here."
- Capability 2: decision-framed club analysis (reframe the vague question, then take a
  position and name what would change it).
- Capability 3: financial–tactical synthesis with wage-scale discipline and a required
  entanglement flag when a tactical problem is a financial constraint.
- Capability 4: fan-register honesty — verdict first, jargon last or not at all.
- Five on-demand reference files:
  - `reference-wilson-tactical-history.md` — Wilson, *Inverting the Pyramid*
  - `reference-cox-premier-league-eras.md` — Cox, *The Mixer*
  - `reference-cox-european-styles.md` — Cox, *Zonal Marking*
  - `reference-szymanski-money-and-soccer.md` — Szymanski, *Money and Soccer*
  - `reference-kuper-szymanski-soccernomics.md` — Kuper & Szymanski, *Soccernomics*
- Repository scaffolding: `README.md`, `LICENSE` (MIT), `.gitignore`, `CHANGELOG.md`.

[Unreleased]: https://github.com/ariel-lee-1023/soccer-analyst/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ariel-lee-1023/soccer-analyst/releases/tag/v1.0.0
