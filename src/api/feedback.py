from fastapi import APIRouter, HTTPException
import sqlite3
import os
from pydantic import BaseModel
from typing import List

router = APIRouter()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(BASE_DIR, "src", "database", "transactions.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


class FeedbackIn(BaseModel):
    transaction_id: str
    is_correct: bool


@router.post("/api/feedback")
def submit_feedback(payload: FeedbackIn):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO feedback (transaction_id, is_correct) VALUES (?, ?)",
            (payload.transaction_id, 1 if payload.is_correct else 0),
        )
        conn.commit()
        return {"status": "ok", "inserted_id": cur.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


@router.get("/api/feedback")
def list_feedback(limit: int = 50, offset: int = 0):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM feedback ORDER BY timestamp DESC LIMIT ? OFFSET ?", (limit, offset))
        rows = [dict(r) for r in cur.fetchall()]
        return rows
    finally:
        conn.close()
