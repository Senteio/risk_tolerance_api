# ChatGPT Code Journal for risk_tolerance_api

## Doc Snapshot – Phase III (2025-08-31)
### Phase III Layout
risk_tolerance_api/
├─ core/
│  └─ scoring.py
├─ backend/
│  └─ index.py
├─ frontend/
│  └─ risk_tolerance_app.py
├─ requirements.txt
├─ .gitignore
└─ README.md

**Permalinks:**
Permalinks:
- [README_v2.md – Phase I – 2025-08-12](https://github.com/Senteio/risk_tolerance_api/blob/69508af7388d2175d45f849a5cadc89d005d26dc/README_v2.md)
- [index.py – Phase I – 2025-08-12](https://github.com/Senteio/risk_tolerance_api/blob/69508af7388d2175d45f849a5cadc89d005d26dc/index.py)

## Phase II – Tag Snapshot
- GitHub Tag: [phase-ii](https://github.com/Senteio/risk_tolerance_api/tree/phase-ii)
- App file at Phase II: [risk_tolerance_app.py](https://github.com/Senteio/risk_tolerance_api/blob/phase-ii/risk_tolerance_app.py)
- Index file at Phase II: [index.py](https://github.com/Senteio/risk_tolerance_api/blob/phase-ii/index.py)
- Commit permalink: [a3936b3](https://github.com/Senteio/risk_tolerance_api/commit/a3936b3)

Notes: Phase II added matplotlib integration, updated requirements, and pie chart visualization.



**Key Points from README:**
- **Purpose:** REST API that returns a 0–100 risk score and risk band (Conservative / Moderate / Aggressive).
- **Setup:**  
  ```bash
  python -m venv venv
   .\venv\Scripts\activate   # or source .venv/bin/activate on Mac/Linux
  pip install -r requirements.txt
Run:

bash
Copy
Edit
uvicorn index:app --reload --port 8000
Config: .env variables like MODEL_PATH, LOG_LEVEL, ALLOWED_ORIGINS.

Endpoints overview: /assess, /health.

Constraints: Stateless; no persistence in Phase I.

API Contract (from index.py):

http
Copy
Edit
POST /assess
Request: { age:int, horizon_years:int, loss_tolerance:string, volatility_pref:string }
Response: { score:int, band:string, explanations:string[] }

GET /health
Response: { status:"ok" }
Terminal Commands:

bash
Copy
Edit
# Run locally
uvicorn index:app --reload --port 8000

# Run tests
pytest -q

# Optional: format/lint
black . && ruff check .
## For Phase II - pie chart phase:
### First start a branch off the main for phase II
If you create a new branch from main, that branch will include everything you’ve done so far — and you can safely build Phase II (pie chart, Plotly, etc.) on top of it.

That’s exactly how feature branching usually works:

main = stable version

phase-ii (new branch) = experiments / additions

🛠 How to do it

From your project folder in terminal (with venv active or not, doesn’t matter for Git):
```
git checkout -b phase-ii
```

This does two things at once:
Creates a new branch called phase-ii
Switches you onto it

Now any changes you make (installing Plotly, modifying risk_tolerance_app.py) will belong to this branch.

🌱 Workflow suggestion

Stay on phase-ii while you add Plotly + pie chart

Commit and push:
```
git add .
git commit -m "Add Plotly pie chart for portfolio allocation"
git push --set-upstream origin phase-ii
```
When you create a new branch (phase-ii)
By default, Git only makes the branch local.
Git doesn’t automatically know if you want that new branch on GitHub too, or if it’s just an experimental local branch.
So the first time you push a new branch, Git asks you to explicitly set the upstream.
That’s why you had to do:
```
git push --set-upstream origin phase-ii
```
After this one-time setup, you can push/pull from phase-ii with just:
```
git push
git pull
```
Later, when you’re happy, you can merge phase-ii back into main either:

On GitHub (Pull Request, clean & visual)

Or locally with git checkout main && git merge phase-ii
### Now let's install plotly
- while in venv mode, under risk_tolerance_api folder:  import plotly from the terminal
- Got a fatal error in venv mode. venv corrupted - see master journal on how to fix this.
I removed venv and reinstalled it then I:
reinstalled my requirements by:
```
pip install -r requirements.txt
```
Then I added plotly:
```
pip install plotly
```
Then we froze the dependencies
- run pip freeze to freeze dependencies
```
pip freeze > requirements.txt
```
### How to tag the project at this point (phase-ii)
```
git checkout main
git pull origin main
git tag -a phase-ii -m "Phase II: pie chart + matplotlib + reqs"
# If you haven't deleted the phase ii branch yet, do that before you push or will get an error
git branch -a
git branch -D phase-ii
git push origin phase-ii
#or push all tags
git push origin --tags
```
### How do I update my tag if I changed something in a phase of my project.
First, delete the local tag
```
git tag -d phase-ii
```
Recreate the latest commit
```
git tag phase-ii
```
Delete the tag on Github
```
git push origin :refs/tags/phase-ii
```
Push the new tag
```
git push origin phase-ii
```
#### This will update the phase-ii tag to point to your latest, cleaned-up commit — with all permalinks included.

### Starting Phase III
- At the point phase-ii worked, start the new branch
```
git checkout -b phase-iii
```
- Double check you are on the branch
```
git branch
```
- you should see:
```
* phase-iii
  main
```
If not then switch branches
```
git switch phase-iii
```
- add then commit any changes you made after the phase-ii tag and before pushing if you did any before the push:
```
git add .
git commit -m "added changes"
```
Then need to push it upstream the first time:
```
git push --set-upstream origin phase-iii
```
## DONT FORGET TO SAVE CHANGES - BEFORE COMMITTING THEM.
#### If a change gets out of sequence from a push, remember this in your bag of tricks:
 From inside the repo root (should be .../risk_tolerance_api)
 ```
git rev-parse --show-toplevel
```
#### See exactly what’s unstaged vs staged
```
git status
git diff                 # unstaged changes
git diff --staged        # staged changes
```

#### Stage the WHOLE file (not just a hunk)
```
git add CHATGPT_CODE_JOURNAL.md
```
#### Commit and confirm the file is included
git commit -m "Journal: update upstream cmd to phase-iii"
git show --name-status HEAD

#### Push to the branch you’re on (phase-iii)
```
git push
```
### Prep for deploy to Streamlit
- Loaded Python 3.12.6. Didn't load newest version because: Most packages (like Streamlit, Pandas, Plotly, etc.) are officially tested with Python 3.11 and 3.12. 3.13 is brand new and may cause compatibility hiccups.