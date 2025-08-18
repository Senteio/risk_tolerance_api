import streamlit as st
import requests

# --- optional chart libs ---
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Risk Tolerance Profiler", layout="centered")
st.title("Risk Tolerance Profiler")

# --- Inputs ---
age = st.slider("What is your age?", 18, 80, 40)
horizon = st.slider("Investment horizon (years)", 1, 30, 10)
attitude = st.selectbox("How would you describe your risk attitude?",
                        ["low", "medium", "high"])

# Choose chart library + options
st.subheader("Visualization Options")
lib = st.radio("Chart library", ["Matplotlib", "Plotly"], horizontal=True)
donut = st.checkbox("Donut style (Plotly only)", value=False)

if st.button("Get Risk Score"):
    # --- Call the FastAPI backend ---
    url = "http://127.0.0.1:8000/risk-score"   # make sure uvicorn is running
    data = {
        "age": age,
        "investment_horizon": horizon,
        "risk_attitude": attitude
    }
    try:
        resp = requests.post(url, json=data, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        st.error(f"Could not reach API: {e}")
    else:
        result = resp.json()
        score = result["risk_score"]
        allocation = result["suggested_allocation"]  # e.g. {"stocks":"60%","bonds":"40%"}

        st.success(f"Your Risk Score: {score}")
        st.caption("Suggested Portfolio Allocation:")
        st.json(allocation)

        # --- Prepare data for chart ---
        labels = list(allocation.keys())
        # strip the % and convert to numbers
        values = [float(v.replace("%", "")) for v in allocation.values()]

        st.subheader("Allocation Chart")

        if lib == "Matplotlib":
            # Matplotlib pie (via st.pyplot)
            fig, ax = plt.subplots(figsize=(5, 5))
            wedges, texts, autotexts = ax.pie(
                values,
                labels=labels,
                autopct="%1.0f%%",
                startangle=90
            )
            ax.axis("equal")  # equal aspect ratio = a circle
            st.pyplot(fig)

        else:
            # Plotly pie (via st.plotly_chart)
            fig = px.pie(
                names=labels,
                values=values,
                hole=0.4 if donut else 0.0
            )
            fig.update_traces(textinfo="percent+label")
            st.plotly_chart(fig, use_container_width=True)
