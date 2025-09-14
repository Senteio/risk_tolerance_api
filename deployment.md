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