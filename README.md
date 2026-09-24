# End-to-End Marketing Data Analytics Portfolio Project

Final-year BCom Marketing Management portfolio specializing in data-driven product marketing analytics and growth strategy for local SMEs.
Features an end-to-end commercial optimization case study for a real-time Coco Bliss Bakery & Snacks business based in the University of Pretoria. By engineering data pipelines across Excel and SQL Server, executing predictive product mix profiling in Python (Pandas & Seaborn), and deploying dynamic Power BI dashboards, I transformed raw Inventory, logistics, and pricing data into actionable market intelligence. My analysis audited a 15+ SKU portfolio to eliminate margin leakages safeguarding a combined R2703 net profit and optimized distribution logistics to sharply upscale local market competitiveness.

An enterprise-level inventory and business intelligence pipeline integrating relational database design, Python data engineering pipelines, automated visualization rendering, and dynamic corporate dashboard modeling.

## 🛠️ Architecture Stack
* **Database Engine:** Microsoft SQL Server Express LocalDB (`(localdb)\MSSQLLocalDB`)
* **Database Management:** SQL Server Management Studio (SSMS) & VS Code MSSQL Extension
* **Data Engineering & Automation:** Python (Stable Environment via Launcher)
* **Libraries:** `pyodbc`, `pandas`, `matplotlib`, `seaborn`, `openpyxl`
* **Business Intelligence Dashboard:** Microsoft Power BI Desktop

---

## Phase 1: Database Architecture (T-SQL)
Created a structured, strongly-typed relational table inside a dedicated container database, enforcing an explicit primary key restriction and tracking unit-level performance metrics.

```sql
USE InventoryDB;
GO

-- Clear out existing test architecture profiles safely
DROP TABLE IF EXISTS Products;

-- Build locked production architecture columns
CREATE TABLE Products (
    ProductID NVARCHAR(10) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Quantity INT NOT NULL,
    TotalCost_ZAR DECIMAL(18, 2) NOT NULL,
    SellingPrice_Unit_ZAR DECIMAL(18, 2) NOT NULL,
    TotalRevenue_ZAR DECIMAL(18, 2) NOT NULL,
    IsProfitable BIT NOT NULL,
    Cost_Unit_ZAR DECIMAL(18, 2) NOT NULL,
    Profit_Unit_ZAR DECIMAL(18, 2) NOT NULL,
    TotalProfit_ZAR DECIMAL(18, 2) NOT NULL
);
GO

-- Seed production inventory matrix records
INSERT INTO Products VALUES 
('P001', 'Aquelle', 6, 43.00, 15.00, 90.00, 1, 7.17, 7.83, 47.00),
('P002', 'Seven7UP', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P003', 'Mountain Dew', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P004', 'Miranda', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P005', 'Pepsi', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P006', 'Sparkling Water', 6, 0.00, 10.00, 60.00, 1, 0.00, 10.00, 60.00),
('P007', '3C Waters', 24, 5.00, 10.00, 240.00, 1, 0.21, 9.79, 235.00),
('P008', 'Simba', 0, 0.00, 0.00, 0.00, 0, 0.00, 0.00, 0.00),
('P009', 'Doritos', 48, 440.00, 12.00, 576.00, 1, 9.17, 2.83, 136.00),
('P010', 'Nik Naks', 48, 0.00, 3.00, 144.00, 0, 0.00, 3.00, 144.00),
('P011', 'Maynards', 24, 250.00, 15.00, 360.00, 1, 10.42, 4.58, 110.00),
('P012', 'Sour Worms', 24, 250.00, 15.00, 360.00, 1, 10.42, 4.58, 110.00),
('P013', 'Peanuts', 36, 190.00, 8.00, 288.00, 1, 5.28, 2.72, 98.00),
('P014', 'Popcorn', 12, 87.00, 15.00, 180.00, 0, 7.25, 7.75, 93.00),
('P015', 'Toppers', 12, 110.00, 15.00, 180.00, 0, 9.17, 5.83, 70.00);
GO
```

---

##  Phase 2: Python Data Engineering Pipelines
Automated the retrieval of relational data and calculated dynamic business performance metrics across cross-source environments.

### Execution Command via Launcher:
```bash
py inventory_chart.py
py marketing_roi_report.py
```

### Script: Profit Margin Percentage Visualization (`inventory_chart.py`)
```python
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=InventoryDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    query = "SELECT ProductName, Cost_Unit_ZAR, Profit_Unit_ZAR FROM Products WHERE Cost_Unit_ZAR > 0;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Dynamic algorithmic transformation
    df["ProfitMargin_Percent"] = (df["Profit_Unit_ZAR"] / df["Cost_Unit_ZAR"]) * 100
    df = df.sort_values(by="ProfitMargin_Percent", ascending=False)

    plt.figure(figsize=(12, 7))
    sns.set_theme(style="whitegrid")
    chart = sns.barplot(x="ProfitMargin_Percent", y="ProductName", data=df, palette="magma", hue="ProductName", legend=False)
 
    plt.title("Product Profit Margin Efficiency (%)", fontsize=16, fontweight="bold", pad=15)
    plt.xlabel("Profit Margin Percentage (%)", fontsize=12, fontweight="bold")
    plt.ylabel("Product Name", fontsize=12, fontweight="bold")
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.1f%%', padding=5, fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.savefig("product_margin_efficiency_chart.png", dpi=300)
    plt.show()
except Exception as e:
    print(f"Failed: {e}")
```

---

## Phase 3: Business Intelligence Modeling (Power BI)
Modeled cross-functional data relationships and deployed user interactivity enhancements.

### 📐 DAX Structural Metric
```dax
Profit Margin % = 
DIVIDE(
    SUM(Products[Profit_Unit_ZAR]), 
    SUM(Products[Cost_Unit_ZAR]), 
    0
) * 100
```
* **Data Modeling:** Linked relational `Products` table from SQL Server database to independent flat `marketing_costing.xlsx` data on `ProductName` column (1-to-1/1-to-Many join).
* **Interactivity Controls:** Integrated global dynamic Slicer dropdown filtering on `ProductName` and .
* **Visual Formatting Rules:** Implemented conditional gradient ranges mapping the low-margin floor to soft amber/red scales and peak performance efficiency metrics to vibrant executive greens.

    
