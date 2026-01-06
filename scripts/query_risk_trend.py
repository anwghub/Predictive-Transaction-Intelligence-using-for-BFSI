import sqlite3
import os

db_path = os.path.join(os.getcwd(), "src", "database", "transactions.db")
print("DB:", db_path)
conn = sqlite3.connect(db_path)
c = conn.cursor()

query = """
SELECT DATE(created_at) AS date,
       AVG(risk_score) AS avg_risk_score
FROM fraud_alerts
GROUP BY DATE(created_at)
ORDER BY DATE(created_at)
"""

print("\nRunning aggregation query:\n", query)
for row in c.execute(query):
    print(row)

conn.close()
