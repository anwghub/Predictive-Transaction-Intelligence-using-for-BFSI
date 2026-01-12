from dotenv import load_dotenv
import os

load_dotenv()
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware


class StripControlCharsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        scope = request.scope
        # remove literal control chars from decoded path
        path = scope.get("path")
        if isinstance(path, str) and ("\n" in path or "\r" in path):
            scope["path"] = path.replace("\n", "").replace("\r", "")
        # raw_path is bytes; strip control bytes if present
        raw_path = scope.get("raw_path")
        if isinstance(raw_path, (bytes, bytearray)):
            if b"\n" in raw_path or b"\r" in raw_path:
                scope["raw_path"] = raw_path.replace(b"\n", b"").replace(b"\r", b"")
        return await call_next(request)
from src.api.transactions import router as transaction_router
from src.preprocessing.cleaning_pipeline import pipeline
from src.preprocessing.train_test_split import create_train_test_split
from src.database.db import create_fraud_alerts_table, create_transactions_table, insert_processed_data, create_feedback_table
from src.api.predict import router as predict_router
from src.api.feedback import router as feedback_router
from src.api.metrics import router as metrics_router
from src.api.alerts import router as alert_router
from src.ml.train_model import train
from src.api.auth import router as auth_router



app = FastAPI(title="Transaction API Backend")

# Add middleware to sanitize incoming paths (strip newline/control chars)
app.add_middleware(StripControlCharsMiddleware)

# Register API routes
app.include_router(auth_router)
app.include_router(transaction_router)
app.include_router(feedback_router)
app.include_router(predict_router)
app.include_router(metrics_router)
app.include_router(alert_router)


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.on_event("startup")
def run_pipeline_on_start():
    env = os.getenv("ENV", "production")

    if env == "local":
        print("Running preprocessing & training pipeline (LOCAL ONLY)")

        pipeline()
        create_train_test_split()

        create_transactions_table()
        create_fraud_alerts_table()
        create_feedback_table()
        insert_processed_data()

        train()
    else:
        print("Production mode: skipping preprocessing & training")

    

