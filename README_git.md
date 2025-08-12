# Risk Tolerance API + Streamlit UI

A tiny FastAPI backend that scores risk tolerance and a Streamlit UI to visualize the allocation.

## Quickstart
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn index:app --reload   # backend
# in another terminal
streamlit run risk_tolerance_app.py
