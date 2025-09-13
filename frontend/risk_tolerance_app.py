# frontend/risk_tolerance_app.py
import os, sys
import requests
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# make repo root importable when running from frontend/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from core.scoring import compute_score

API_BASE_URL = os.getenv("API_BASE_URL")  # set in Streamlit Secrets later

st.set_page_config(page_title="Risk Tolerance Profiler")
st.title("Risk Tolerance Profiler")

# --- Inputs ---
age = st.slider("What is your age?", 18, 80, 40)
horizon = st.slider("Investment horizon (years)", 1, 30, 12)
attitude = st.selectbox("How would you describe your risk attitude?",
                        ["low", "medium", "high"])

st.subheader("Visualization Options")
lib = st.radio("Chart library", ["Matplotlib", "Plotly"], index=1, horizontal=True)
donut = st.checkbox("Donut style (Plotly only)")

def get_result(age, horizon, attitude):
    # Try cloud API first if configured
    if API_BASE_URL:
        try:
            r = requests.post(
                f"{API_BASE_URL}/risk-score",
                json={"age": age, "investment_horizon": horizon, "risk_attitude": attitude},
                timeout=6,
            )
            r.raise_for_status()
            data = r.json()
            return data["risk_score"], data["suggested_allocation"], None
        except Exception as e:
            return None, None, f"Could not reach API at {API_BASE_URL}: {e}"

    # Fallback: compute locally
    score, alloc = compute_score(age, horizon, attitude)
    return score, alloc, None

if st.button("Get Risk Score"):
    score, alloc, err = get_result(age, horizon, attitude)

    if err and score is None:
        st.error(err)
        st.info("Falling back to local scoring logic.")
        score, alloc = compute_score(age, horizon, attitude)

    st.success(f"Your Risk Score: {score}")
    st.json({"Suggested Portfolio Allocation": alloc})

    # --- Chart ---
    labels = list(alloc.keys())
    values = [float(v.replace("%", "")) for v in alloc.values()]

    if lib == "Matplotlib":
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.0f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
    else:
        hole = 0.4 if donut else 0.0
        fig = px.pie(values=values, names=labels, hole=hole)
        st.plotly_chart(fig, use_container_width=True)
