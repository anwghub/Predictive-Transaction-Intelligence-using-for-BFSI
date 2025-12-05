import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
import os
import json

# ---------------------------------------------------
# Correct project base directory
# ---------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# ---------------------------------------------------
# Correct paths for processed data & model save
# ---------------------------------------------------
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "transactions_processed.csv")

MODEL_PATH = os.path.join(BASE_DIR, "src", "ml", "fraud_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "src", "ml", "scaler.pkl")
METRICS_PATH = os.path.join(BASE_DIR, "src", "ml", "metrics.json")

# Ensure ml folder exists
os.makedirs(os.path.join(BASE_DIR, "src", "ml"), exist_ok=True)

def load_data():
    return pd.read_csv(PROCESSED_PATH)

def train():
    df = load_data()

    # Features
    X = df[[
        "kyc_verified",
        "account_age_days",
        "transaction_amount",
        "hour",
        "weekday",
        "month",
        "is_high_value"
    ]]

    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred)),
        "recall": float(recall_score(y_test, y_pred)),
        "f1_score": float(f1_score(y_test, y_pred)),
        "auc": float(roc_auc_score(y_test, y_prob))
    }

    # ---------------------------------------------------
    # FIX 3: Save model & scaler correctly
    # ---------------------------------------------------
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    print("\nModel trained & saved successfully:")
    print(f"Model: {MODEL_PATH}")
    print(f"Scaler: {SCALER_PATH}")
    print(f"Metrics: {METRICS_PATH}")
    print(metrics)
