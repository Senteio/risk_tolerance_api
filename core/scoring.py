# core/scoring.py
def compute_score(age: int, horizon: int, attitude: str):
    base = 0
    base += min(max((80 - age) // 10, 0), 5)                 # younger -> higher
    base += min(horizon // 5, 5)                             # longer horizon -> higher
    base += {"low": 0, "medium": 2, "high": 4}.get(attitude, 0)
    score = int(max(1, min(10, base)))

    if score <= 3:
        alloc = {"stocks": "20%", "bonds": "80%"}
    elif score <= 6:
        alloc = {"stocks": "40%", "bonds": "60%"}
    elif score <= 8:
        alloc = {"stocks": "60%", "bonds": "40%"}
    else:
        alloc = {"stocks": "80%", "bonds": "20%"}
    return score, alloc
