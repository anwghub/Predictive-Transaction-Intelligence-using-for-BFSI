from fastapi import APIRouter
import sqlite3
import pandas as pd
from fastapi.responses import StreamingResponse
from io import StringIO
import os

router = APIRouter()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(BASE_DIR, "src", "database", "transactions.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# 1️⃣ Get transactions (with filters)
@router.get("/api/transactions")
def get_transactions(limit: int = 50, offset: int = 0, fraud_only: bool = False):
    conn = get_connection()

    query = "SELECT * FROM transactions"
    if fraud_only:
        query += " WHERE is_fraud = 1"

    query += " ORDER BY timestamp DESC LIMIT ? OFFSET ?"

    df = pd.read_sql_query(query, conn, params=(limit, offset))
    conn.close()

    return df.to_dict(orient="records")



# 3️⃣ Recent transactions (real-time feed)
@router.get("/api/transactions/recent")
def recent_transactions(limit: int = 10):
    conn = get_connection()

    query = """
    SELECT 
        t.transaction_id,
        t.customer_id,
        t.transaction_amount AS amount,
        t.timestamp,
        -- prefer exact transaction_id match; otherwise, use most recent customer alert within 24 hours
        COALESCE(
            (
                SELECT fa.risk_score
                FROM fraud_alerts fa
                WHERE fa.transaction_id = t.transaction_id
                ORDER BY fa.created_at DESC
                LIMIT 1
            ),
            (
                SELECT MAX(fa2.risk_score)
                FROM fraud_alerts fa2
                WHERE fa2.customer_id = t.customer_id
                  AND abs(strftime('%s', fa2.created_at) - strftime('%s', t.timestamp)) <= 86400
            ),
            0
        ) AS risk_score,
        CASE WHEN (
                EXISTS(
                    SELECT 1 FROM fraud_alerts fa3
                    WHERE fa3.transaction_id = t.transaction_id
                ) OR EXISTS (
                    SELECT 1 FROM fraud_alerts fa4
                    WHERE fa4.customer_id = t.customer_id
                      AND abs(strftime('%s', fa4.created_at) - strftime('%s', t.timestamp)) <= 86400
                )
            ) THEN 1 ELSE 0 END AS is_fraud
    FROM transactions t
    ORDER BY t.timestamp DESC
    LIMIT ?
    """

    df = pd.read_sql_query(query, conn, params=(limit,))
    conn.close()

    return df.to_dict(orient="records")


# 4️⃣ Risk trend over time (Milestone 3 / 4)
@router.get("/api/transactions/analytics/risk-trend")
def risk_trend():
    conn = get_connection()

    query = """
    SELECT DATE(created_at) AS date,
           AVG(risk_score) AS avg_risk_score
    FROM fraud_alerts
    GROUP BY DATE(created_at)
    ORDER BY DATE(created_at)
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df.to_dict(orient="records")



# 5️⃣ Download transactions as CSV (Milestone 1 premium feature)
@router.get("/api/transactions/download/csv")
def download_transactions_csv():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    output = StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"}
    )


# 2️⃣ Get transaction by ID
@router.get("/api/transactions/{transaction_id}")
def get_transaction_by_id(transaction_id: str):
    conn = get_connection()

    query = "SELECT * FROM transactions WHERE transaction_id = ?"
    df = pd.read_sql_query(query, conn, params=(transaction_id,))
    conn.close()

    if df.empty:
        return {"error": "Transaction not found"}

    return df.iloc[0].to_dict()
