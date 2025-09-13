# backend/index.py
# For deployment later with Render
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from core.scoring import compute_score

app = FastAPI(title="Risk Tolerance API", version="0.2.0")

# Allow your Streamlit app (tighten origins later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inputs(BaseModel):
    age: int
    investment_horizon: int
    risk_attitude: str

@app.get("/health")
def health():
    return {"ok": True, "version": app.version}

@app.post("/risk-score")
def risk_score(inp: Inputs):
    score, alloc = compute_score(inp.age, inp.investment_horizon, inp.risk_attitude)
    return {"risk_score": score, "suggested_allocation": alloc}
