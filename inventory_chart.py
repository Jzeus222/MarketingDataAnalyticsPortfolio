import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn_str = ( 
     "DRIVER={ODBC Driver 17 for SQL Server};"
     "SERVER=(Localdb)\\MSSQLLocalDB;"
     "DATABASE=InventoryDB;"
     "Trusted_Connection=yes;"
     "TrustServerCertificate=yes;"
)   

try:
    print("Reading data from SQL Server to calculate profit margins...")
    conn = pyodbc.connect(conn_str)

    query = """
        SELECT ProductName, Cost_Unit_ZAR, Profit_Unit_ZAR
        FROM Products
        WHERE Cost_Unit_ZAR > 0;
    """

    df = pd.read_sql(query, conn)
    

except Exception as error:
    print(f"Analytics calculation process failed: {error}")

else:
    print("\n--- DEBUG 3C WATERS DATA ---")
    print(df[df["ProductName"] == "3C Waters"][["ProductName", "Profit_Unit_ZAR", "Cost_Unit_ZAR"]])
    df["ProfitMargin_Percent"] = (df["Profit_Unit_ZAR"] / df["Cost_Unit_ZAR"]) * 100
    
    df = df.sort_values(by="ProfitMargin_Percent", ascending=False)

    plt.figure(figsize=(12, 7))
    sns.set_theme(style="whitegrid")
    
    chart = sns.barplot(
    x="ProfitMargin_Percent",
    y="ProductName",
    data=df,
    palette="magma",
    hue="ProductName",
    legend=False
)

    plt.title("Product Profit Margin Efficiency (%)", fontsize=16, fontweight="bold", pad=15)
    plt.xlabel("Profit Margin Percentage (%)", fontsize=12, fontweight="bold")
    plt.ylabel("Product Name", fontsize=12, fontweight="bold")
    plt.tight_layout()

    for container in chart.containers:
        chart.bar_label(container, fmt='%.1f%%', padding=5, fontsize=10, fontweight="bold")

    plt.savefig("product_margin_efficiency_chart.png", dpi=300)
    print("Success: Performance chart saved as 'product_margin_efficiency_chart.png'!")

    plt.show()

finally:
    if "conn" in locals():
        conn.close()