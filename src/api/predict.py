from fastapi import APIRouter
import joblib
import pandas as pd
import os

router = APIRouter()

# --------------------------------------
# Absolute path based on predict.py
# --------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "fraud_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "ml", "scaler.pkl")

print("MODEL PATH:", MODEL_PATH)
print("SCALER PATH:", SCALER_PATH)

# Load safely
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@router.post("/api/predict")
def predict_transaction(data: dict):

    df = pd.DataFrame([data])

    # Required features
    feature_cols = [
        "kyc_verified",
        "account_age_days",
        "transaction_amount",
        "hour",
        "weekday",
        "month",
        "is_high_value"
    ]

    # Select features
    features = df[feature_cols]

    # Scale
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]
    risk_score = float(model.predict_proba(scaled_features)[0][1])

    return {
        "prediction": "Fraud" if prediction == 1 else "Legit",
        "is_fraud": bool(prediction),
        "risk_score": risk_score
    }
