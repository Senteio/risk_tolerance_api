# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## \[Unreleased]

* Placeholder for changes not yet tagged.

---

## [v0.3.0] - 2025-09-12

### Added

* Phase III deployed to Streamlit Cloud.
* Added `/docs/deployment.md` runbook for repeatable deployments.
* Introduced secrets management for API keys in Cloud (moved secrets out of code).

### Changed

* Pinned dependencies in `requirements.txt` for Cloud compatibility.

### Fixed

* Resolved OneDrive lockfile issue by moving repo outside sync / pausing sync during git ops.

---

## [v0.2.0] - 2025-08-20

### Added

* Phase II dashboards and interactive visualizations.
* First draft of `CHATGPT_Code_JOURNAL.md` to track session-by-session work.

### Changed

* Restructured project to support modularized code and clearer imports.

---

## [v0.1.0] - 2025-07-05

### Added

* Phase I initial API implementation (risk tolerance prototype).
* Base README and setup instructions.

---

<!-- 🔗 Release Links (GitHub compare/tag) -->

<!-- Keep link refs at the very bottom so markdown autolinks resolve. Do not add content below this block. -->

[v0.3.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.1.0...v0.2.0
[v0.1.0]: https://github.com/Senteio/risk_tolerance_api/releases/tag/v0.1.0
