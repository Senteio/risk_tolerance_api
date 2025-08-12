# index.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 📥 Define expected input
class RiskAnswers(BaseModel):
    age: int
    investment_horizon: int  # in years
    risk_attitude: str       # "low", "medium", or "high"

# 🧠 Suggest allocation based on score
def suggest_allocation(score):
    if score >= 8:
        return {"stocks": "80%", "bonds": "20%"}
    elif score >= 5:
        return {"stocks": "60%", "bonds": "40%"}
    else:
        return {"stocks": "40%", "bonds": "60%"}

# 🚀 Route to calculate risk
@app.post("/risk-score")
def calculate_risk_score(data: RiskAnswers):
    score = 0

    if data.age < 35:
        score += 2
    elif data.age < 50:
        score += 1

    if data.investment_horizon > 10:
        score += 3
    elif data.investment_horizon > 5:
        score += 1

    if data.risk_attitude.lower() == "high":
        score += 5
    elif data.risk_attitude.lower() == "medium":
        score += 3
    else:
        score += 1

    allocation = suggest_allocation(score)

    return {
        "risk_score": score,
        "suggested_allocation": allocation
    }
