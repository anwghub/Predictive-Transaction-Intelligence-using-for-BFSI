import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_explanation(data, prediction, risk_score, reasons):
    prompt = f"""
Explain this transaction decision in simple language.

Transaction Details:
Amount: {data['transaction_amount']}
Channel: {data['channel']}
KYC: {data['kyc_verified']}
Time: {data['timestamp']}

Prediction: {prediction}
Risk Score: {risk_score}

Rules Triggered: {', '.join(reasons) if reasons else 'None'}
"""

    return model.generate_content(prompt).text.strip()
