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

### Added
- Completed Phase II functionality.
- Documentation updates in CODE_JOURNAL.md.

- **Journal Permalink** → [View Journal at Phase II](https://github.com/Senteio/risk_tolerance_api/blob/fa6db53e3a2e6f2fd5979b9be1f7bda244bdf141/CODE_JOURNAL.md)
- **Commit Permalink** → [View Code at Phase II](https://github.com/Senteio/risk_tolerance_api/commit/fa6db53e3a2e6f2fd5979b9be1f7bda244bdf141)

✅ Snapshot of both the written documentation and the repo state at this milestone.


---

## [v0.1.0] - 2025-07-05

### Added

* Phase I initial API implementation (risk tolerance prototype).
* Base README and setup instructions.

---

# Changelog

All notable changes to this project will be documented in this file.  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

---

## [1.0.0] - 2025-09-17
### Added
- Initial deployment of `risk_tolerance_api` to Streamlit Cloud.
- Created `Financial.code-workspace` file to manage financial projects in VS Code.
- Desktop shortcut for one-click launch into the financial workspace.

### Changed
- Consolidated folder structure under:
C:\dev\repos\financial_workspace\

markdown
Copy code
- Moved repo out of OneDrive to prevent sync conflicts.

### Removed
- Deleted obsolete `phase-iii` branch post-deployment.
- Removed duplicate repo previously stored in OneDrive.

<!-- 🔗 Release Links (GitHub compare/tag) -->

<!-- Keep link refs at the very bottom so markdown autolinks resolve. Do not add content below this block. -->

[v0.3.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.1.0...v0.2.0
[v0.1.0]: https://github.com/Senteio/risk_tolerance_api/releases/tag/v0.1.0
