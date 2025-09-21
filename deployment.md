Save all files (Ctrl+S in VS Code).

git status → make sure modified files show.

git add -A

git commit -m "..."

git push origin <branch>

Refresh GitHub → check Preview tab shows the new contents.

# Deployment Runbook (Phase III → Cloud → Main)


1. **Prep**
- `pip freeze | sort > requirements.txt`
- Verify local: `streamlit run streamlit_app.py`
2. **Deploy to Cloud (branch = phase-iii)**
- Set **App file**; paste **Secrets**; Deploy.
- QA smoke.
3. **Merge → main**
- `git checkout main && git pull`
- `git merge --no-ff phase-iii -m "Merge: Phase III release"`
- `git push origin main`
4. **Tag**
- `git tag -a v0.3.0 -m "Phase III release" && git push origin v0.3.0`
5. **Switch Cloud to main** and **Redeploy**
6. **Changelog** + update README links.

### The fol was added by Chat - I kept above redundant info just in case

# Deployment Runbook

## Pre-commit / Pre-merge Quick Check
- Save all files (Ctrl+S in VS Code).
- `git status` → modified files should show.
- Stage, commit, and push:
  ```bash
  git add -A
  git commit -m "..."
  git push origin <branch>
Refresh GitHub → Preview tab shows new contents.

Streamlit Cloud (current UI)
New app or switching branches:

Create app → Deploy public app from GitHub

Repo: Senteio/risk_tolerance_api

Branch: choose your target (phase-iv for staging, main for prod)

Main file path: frontend/risk_tolerance_app.py

App URL: must be unique (you can reclaim the old URL by renaming or deleting the previous app)

Paste Secrets (copy from staging/prod as appropriate)

Deploy → watch logs

Post-deploy QA (smoke test):

App loads and primary flow works end-to-end

Secrets-dependent features OK

Logs show no missing packages or noisy warnings

README live link correct

## Phase III → Cloud → Main (reference)
Prep

Update dependencies:

```
pip freeze | sort > requirements.txt
```
Verify local:
```
streamlit run streamlit_app.py
```
## Deploy to Cloud (branch = phase-iii)

Set app file
Paste secrets
Deploy → QA smoke

## Merge to main
```
git checkout main && git pull
git merge --no-ff phase-iii -m "Merge: Phase III release"
git push origin main
```
## Tag
```
git tag -a v0.3.0 -m "Phase III release"
git push origin v0.3.0
```
## Switch Cloud app to main

Redeploy from main to ensure it still works

## Changelog

Move [Unreleased] changes into ## [v0.3.0]

Update README links

# Phase IV Release Checklist → v0.4.0
While developing on phase-iv

Keep notes under [Unreleased] in CHANGELOG.md (Added/Changed/Fixed/Removed)

## At release time

### Merge to main
```
git checkout main && git pull
git merge --no-ff phase-iv -m "Merge: Phase IV release"
git push origin main
```
### Cut changelog

Move items from [Unreleased] → ## [v0.4.0] - YYYY-MM-DD

Leave an empty [Unreleased] at top

### Tag on main

Git Bash / PowerShell (I use CMD...see below):
```
git checkout main && git pull
git tag -a v0.4.0 -m "Phase IV release"
git push origin v0.4.0
```
#### Windows CMD (same commands work; just use ~1 instead of ^1 when referencing parents) -- this is me.

### Update link refs at bottom of CHANGELOG.md

```
[Unreleased]: https://github.com/Senteio/risk_tolerance_api/compare/v0.4.0...HEAD
[v0.4.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.3.0...v0.4.0
[v0.3.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/Senteio/risk_tolerance_api/compare/v0.1.0...v0.2.0
[v0.1.0]: https://github.com/Senteio/risk_tolerance_api/releases/tag/v0.1.0
```
### Deploy prod from main

Streamlit Cloud → Create app → Deploy from GitHub

Branch: main, File path: frontend/risk_tolerance_app.py, URL = prod URL

### Clean branches (optional)
```
git branch -d phase-iv
git push origin --delete phase-iv
git checkout -b phase-v
```
# Notes & Gotchas
Always tag on main after merge (tags = deployed code).

Windows CMD: use ~1 instead of ^1 (3730b6a~1) because ^ is a special escape char.

If CHANGELOG.md compare links show “nothing to compare,” ensure all earlier tags (v0.1.0, v0.2.0, etc.) exist and point to correct commits.

Keep link references at the very bottom of CHANGELOG.md so Markdown auto-links resolve.



#### Failure Playbook goes at the very bottom of deployment.md

# Failure Playbook (Common Errors & Fixes)

### 1. `.git/index.lock` prevents commit/rebase
- Error: `fatal: Unable to create '.git/index.lock': File exists`
- Cause: a previous Git process crashed or was interrupted.
- Fix:
  ```bash
  rm -f .git/index.lock
(On Windows CMD: del .git\index.lock)

2. Windows CMD swallows ^ in revspecs
Symptom: fatal: ambiguous argument '3730b6a1' as a valid ref

Cause: ^ is treated as an escape in CMD.

Fix: use ~1 instead of ^1 (e.g., 3730b6a~1) or run commands in Git Bash/PowerShell.

3. Streamlit Cloud missing package error
Symptom: app fails to deploy with ModuleNotFoundError

Fix: update requirements.txt before committing:
```
pip freeze | sort > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```
4. Changelog compare links show “Nothing to compare”
Symptom: GitHub compare view says nothing to compare.

Cause: missing or misaligned tags.

Fix:

Ensure each phase has a tag on main after merge.

Backfill tags if needed:
```
git tag -a v0.2.0 <SHA> -m "Phase II release"
git push origin v0.2.0
```
5. Streamlit Cloud: app URL conflict
Symptom: Cannot reuse old subdomain when deploying a new branch.

Fix:

Rename or delete the old app under App Settings → General

Reclaim the subdomain in the new deployment.

6. Accidental unpushed commits
Symptom: GitHub doesn’t show local changes after commit.

Fix:
```
git push origin <branch>
```
Double-check with 
```
git log origin/<branch> 
```
vs 
```
git log <branch>
```

# Deployment Notes

## Repository Cleanup
- Removed the stale **`phase-iii` branch** after completing deployment to Streamlit Cloud.  
- Deleted the duplicate **risk_tolerance_api repo** that was synced through OneDrive to prevent conflicts.  

---

## Folder Structure
Development work is consolidated under:

C:\dev\repos
└── financial_workspace\ ← container folder (not a repo)
└── risk_tolerance_api\ ← active GitHub repo

swift
Copy code

- `financial_workspace` is used only as a container for financial projects.  
- `risk_tolerance_api` remains the primary GitHub repository.  

---

## VS Code Workspace Setup
Created a `Financial.code-workspace` file in `C:\dev\repos\`:

```json
{
  "folders": [
    { "path": "C:\\dev\\repos\\financial_workspace" }
  ],
  "settings": {
    "files.exclude": {
      "**/.venv": true,
      "**/__pycache__": true,
      "**/.git": true
    }
  }
}
```
Opening this workspace file loads all repos/projects inside financial_workspace automatically.

Keeps the environment consistent and future-proof as additional repos are added.

Opening the Workspace
Use File → Open Workspace from File… in VS Code.

Select Financial.code-workspace.

Explorer shows the financial_workspace container and its repos (e.g., risk_tolerance_api).

Shortcut for Faster Access
Created a Windows shortcut to launch VS Code directly into the workspace:

swift
Copy code
"C:\Users\steve\AppData\Local\Programs\Microsoft VS Code\Code.exe" "C:\dev\repos\Financial.code-workspace"
Named: Financial Workspace.

Pinned to Taskbar for one-click access.

Streamlit Cloud Deployment
Prerequisites
A GitHub repo (risk_tolerance_api) with all changes committed and pushed.

requirements.txt updated with dependencies.

Main app entry point (e.g., app.py) working locally with streamlit run app.py.

Deployment Steps
Push code to GitHub

bash
Copy code
git add .
git commit -m "Deploying update"
git push origin main
Tag a release (optional but recommended)

bash
Copy code
git tag -a v1.0 -m "First production release"
git push origin v1.0
Log in to Streamlit Cloud

Go to share.streamlit.io.

Connect your GitHub account (if not already connected).

Create a new app

Select the repo: risk_tolerance_api.

Choose the branch: main.

Set the main file path: app.py (or equivalent).

Click Deploy.

Verify deployment

Wait for build to complete.

Open the provided URL to confirm the app runs.

Post-Deployment Notes
Once deployment is successful, delete old feature branches (e.g., phase-iii) to keep the repo clean.

Maintain semantic version tags (v1.0, v1.1, etc.) for traceability.

If updating dependencies, re-deploy with an updated requirements.txt.

yaml
Copy code

---

## Virtual Environment Management

### Auto-Activation in VS Code
- VS Code (with the Python extension) automatically detects a `.venv` folder inside the project and activates it in the integrated terminal.  
- The interpreter path is also defined in `Financial.code-workspace`:

```json
"python.defaultInterpreterPath": "C:\\dev\\repos\\financial_workspace\\risk_tolerance_api\\.venv\\Scripts\\python.exe"
```

## Package Management with requirements.txt

### Installing Packages
Always install new packages **inside the active venv** so they don’t leak into the global Python environment:

```
pip install package_name
Freezing Dependencies
```
After installing or upgrading packages, update requirements.txt so the environment is reproducible:
```
pip freeze > requirements.txt
```
This captures the exact versions of all installed packages.

Rebuilding Environment from requirements.txt
When setting up the project on a new machine (or rebuilding a venv):

```
pip install -r requirements.txt
```
This ensures the new environment matches the original exactly.

Best Practice with Git
✅ Commit requirements.txt to source control.

❌ Do NOT commit .venv/ (should be excluded in .gitignore).

This way, collaborators (or future you) can recreate the environment without shipping unnecessary binaries.

Example Workflow
Activate venv (auto-activated in VS Code).

Install a package:
```
pip install pandas
```
Update requirements.txt:

```
pip freeze > requirements.txt
```
Commit and push:

```
git add requirements.txt
git commit -m "Add pandas dependency"
git push origin main
```

👉 This gives you a **repeatable “from scratch” deployment checklist** inside `deployment.md`.  
Would you like me to also add a **troubleshooting section** (common Streamlit errors: package not found, branch not building, secrets not set, etc.) so you don’t have to dig for fixes when something breaks?

## Post Deployment Notes

### Phase II Milestone (2025-09-05)

- **Journal Permalink** → [View Journal at Phase II](https://github.com/Senteio/risk_tolerance_api/blob/fa6db53e3a2e6f2fd5979b9be1f7bda244bdf141/CODE_JOURNAL.md)
- **Commit Permalink** → [View Code at Phase II](https://github.com/Senteio/risk_tolerance_api/commit/fa6db53e3a2e6f2fd5979b9be1f7bda244bdf141)

✅ Snapshot of both the written documentation and the repo state at this milestone.
