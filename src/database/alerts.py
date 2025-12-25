from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

Base = declarative_base()

class FraudAlert(Base):
    __tablename__ = "fraud_alerts"

    alert_id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String)
    customer_id = Column(String)
    risk_score = Column(Float)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
