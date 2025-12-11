from fastapi import APIRouter, HTTPException, Query
import joblib
import pandas as pd
import os

router = APIRouter()

# Project root (same approach as train_model.py)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODEL_PATH = os.path.join(BASE_DIR, "src", "ml", "fraud_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "src", "ml", "scaler.pkl")

model = None
scaler = None

def load_model_if_needed():
    global model, scaler
    if model is None or scaler is None:
        if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
            raise FileNotFoundError("Model or scaler not found. Train the model first.")
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)


def _predict_from_dict(data: dict):
    """Core prediction logic that expects a dict with feature keys."""
    df = pd.DataFrame([data])

    feature_cols = [
        "kyc_verified",
        "account_age_days",
        "transaction_amount",
        "hour",
        "weekday",
        "month",
        "is_high_value",
    ]

    missing = [c for c in feature_cols if c not in df.columns]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing features: {missing}")

    features = df[feature_cols].copy()

    # Map common boolean-like strings to integers
    bool_map = {"Yes": 1, "No": 0, "Y": 1, "N": 0, "True": 1, "False": 0, True: 1, False: 0}
    for col in ["kyc_verified", "is_high_value"]:
        features[col] = features[col].map(bool_map).fillna(features[col])

    #  numeric columns and validate
    for col in feature_cols:
        features[col] = pd.to_numeric(features[col], errors="coerce")

    if features.isna().any(axis=1).any():
        invalid_cols = features.columns[features.isna().any()].tolist()
        raise HTTPException(status_code=400, detail=f"Invalid or non-numeric values in features: {invalid_cols}")

    try:
        scaled_features = scaler.transform(features)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error scaling features: {ex}")

    prediction = model.predict(scaled_features)[0]
    risk_score = float(model.predict_proba(scaled_features)[0][1]) if hasattr(model, "predict_proba") else 0.0

    return {
        "prediction": "Fraud" if int(prediction) == 1 else "Legit",
        "is_fraud": bool(int(prediction)),
        "risk_score": risk_score,
    }


@router.post("/api/predict")
def predict_transaction(data: dict):
    try:
        load_model_if_needed()
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))

    return _predict_from_dict(data)

