import sqlite3
import os

DB = os.path.join(os.getcwd(), "src", "database", "transactions.db")
print("DB:", DB)

conn = sqlite3.connect(DB)
cur = conn.cursor()

query = """
SELECT t.transaction_id AS t_id, t.timestamp AS t_ts, t.transaction_amount AS t_amount,
       f.alert_id AS f_alert_id, f.transaction_id AS f_id, f.risk_score AS f_risk, f.created_at AS f_created
FROM transactions t
LEFT JOIN fraud_alerts f
  ON t.transaction_id = f.transaction_id
ORDER BY t.timestamp DESC
LIMIT 50
"""

print("Running join query (transactions LEFT JOIN fraud_alerts):")
rows = cur.execute(query).fetchall()
for r in rows:
    print(r)

# Also show transactions that have a matching fraud_alert
print('\nTransactions with matching fraud_alerts:')
query2 = """
SELECT t.transaction_id, COUNT(f.alert_id) as alert_count, MAX(f.risk_score) as max_risk
FROM transactions t
LEFT JOIN fraud_alerts f ON t.transaction_id = f.transaction_id
GROUP BY t.transaction_id
ORDER BY alert_count DESC
LIMIT 20
"""
for r in cur.execute(query2):
    print(r)

conn.close()
