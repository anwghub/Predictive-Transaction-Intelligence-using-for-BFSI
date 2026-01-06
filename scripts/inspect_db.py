import sqlite3
import os
import sys

db_path = os.path.join(os.getcwd(), "src", "database", "transactions.db")
print("Checking DB at:", db_path)
if not os.path.exists(db_path):
    print("DB not found:", db_path)
    sys.exit(1)

conn = sqlite3.connect(db_path)
c = conn.cursor()

print("\nPRAGMA table_info('fraud_alerts'):")
for row in c.execute("PRAGMA table_info('fraud_alerts')"):
    print(row)

print("\nFirst 5 rows from fraud_alerts:")
for row in c.execute("SELECT * FROM fraud_alerts LIMIT 5"):
    print(row)

conn.close()
