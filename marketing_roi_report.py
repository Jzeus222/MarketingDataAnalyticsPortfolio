import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=InventoryDB;"
    "Trusted_Connection=yes;"
    "TrustedServerCertificate=yes;"
)

try:
    print("Extracting sales records from SQL Server...")
    conn = pyodbc.connect(conn_str)
    sql_query = "SELECT ProductName, TotalProfit_ZAR FROM InventoryDB.dbo.Products;"
    db_df = pd.read_sql(sql_query, conn)
    conn.close()
    print("Extracting advertising allocations from marketing_costing.xlsx...")

    excel_df = pd.read_excel("marketing_costing.xlsx")

    merged_df = pd.merge(
        db_df,
        excel_df,
        left_on="ProductName",
        right_on="ProductName",
        how="inner",
    )

    merged_df["Marketing_ROI_Percent"] = (merged_df["TotalProfit_ZAR"] / merged_df["MarketingSpend_ZAR"]) * 100
    merged_df = merged_df.sort_values(by="Marketing_ROI_Percent", ascending=False)

    print("\n--- Consolidate Business Intelligence Portfolio Data---")
    print(merged_df.to_string(index=False))

    chart = sns.barplot(
        x="Marketing_ROI_Percent",
        y="ProductName",
        data=merged_df,
        palette="crest",
        hue="ProductName",
        legend=False
    )

    plt.title("Marketing ROI Performance Analysis (%)", fontsize=16, fontweight="bold", pad=15)
    plt.xlabel("Return on Investment (ROI %)", fontsize=12, fontweight="bold")
    plt.ylabel("Product Portfolio", fontsize=12, fontweight="bold")

    for container in chart.containers:
        chart.bar_label(container, fmt='%.1f%%', padding=5, fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.savefig("marketing_roi_efficiency.png", dpi=300)
    print("\nSuccess: Strategic report saved as 'marketing_roi_efficiency.png'!")
    plt.show()

except Exception as e:
    print(f"Portfolio reporting pipeline failed: {e}")