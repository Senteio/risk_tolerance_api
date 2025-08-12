import streamlit as st
import requests

st.title("Risk Tolerance Profiler")

# Collect input from the user
age = st.slider("What is your age?", 18, 80, 40)
horizon = st.slider("Investment horizon (years)", 1, 30, 10)
attitude = st.selectbox("How would you describe your risk attitude?", ["low", "medium", "high"])

# When the user clicks the button
if st.button("Get Risk Score"):
    # Send data to your local FastAPI endpoint
    url = "http://127.0.0.1:8000/risk-score"
    data = {
        "age": age,
        "investment_horizon": horizon,
        "risk_attitude": attitude
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Your Risk Score: {result['risk_score']}")
        st.write("Suggested Portfolio Allocation:")
        st.write(result["suggested_allocation"])
    else:
        st.error("Something went wrong. Please try again.")
