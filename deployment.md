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