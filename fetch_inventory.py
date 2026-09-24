import pyodbc
import pandas as pd

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=InventoryDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;")

print("Connecting to local SQL database engine...")
conn = pyodbc.connect(conn_str)

query = "SELECT * FROM Products;"

df = pd.read_sql(query, conn)

print("\n--- Connection Successful! Live Dataset Pulled ---")
print(df.to_string(index=False))

try:
  conn.close()

except Exception as e:
    print(f"\nConnection failed! Error details: {e}")