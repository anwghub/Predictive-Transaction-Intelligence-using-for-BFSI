def apply_rules(data):
    reasons = []
    risk_boost = 0.0

    if data["transaction_amount"] > 5 * data["avg_transaction_amount"]:
        reasons.append("Transaction amount exceeds 5x average")
        risk_boost += 0.25

    if data["channel"] == "international" and data["kyc_verified"] == "No":
        reasons.append("International transaction without KYC")
        risk_boost += 0.3

    hour = int(data["timestamp"].split(":")[0])
    if 2 <= hour <= 4:
        reasons.append("Transaction at unusual hours")
        risk_boost += 0.15

    return reasons, risk_boost
