# ChatGPT Code Journal for risk_tolerance_api

## Doc Snapshot – Phase I (2025-08-12)

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
  python -m venv .venv
  . .venv/Scripts/activate   # or source .venv/bin/activate on Mac/Linux
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
- while in venv mode, under risk_tolerance_api folder:  import plotly from the terminal
```
pip install plotly
```
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
