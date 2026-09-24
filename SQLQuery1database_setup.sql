USE InventoryDB;
GO

DROP TABLE IF EXISTS Products;

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

INSERT INTO Products VALUES 
('P001', 'Aquelle', 6, 43.00, 15.00, 90.00, 1, 7.17, 7.83, 47.00),
('P002', 'Seven7UP', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P003', 'Mountain Dew', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P004', 'Miranda', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00),
('P005', 'Pepsi', 12, 116.00, 18.00, 216.00, 1, 9.67, 8.33, 100.00);
GO

SELECT * FROM Products;

INSERT INTO Products VALUES
('P006', 'Sparkiling Water', 6, 0.00, 10.00, 60.00, 1, 0.00, 10.00, 60.00),
('P007', '3C Waters', 24, 5.00, 10.00, 240.00, 1, 0.21, 9.79, 235.00),
('P008', 'Simba', 0, 0.00, 0.00, 0.00, 0, 0.00, 0.00, 0.00),
('P009', 'Doritos', 48, 440.00, 12.00, 576.00, 1, 9.17, 2.83, 136.00),
('P010', 'Nik Naks', 48, 0.00, 3.00, 144.00, 0, 0.00, 3.00, 144.00);
GO

INSERT INTO Products VALUES
('P011', 'Maynards', 24, 250.00, 15.00, 360.00, 1, 10.42, 4.58, 110.0),
('P012', 'Sour Worms', 24, 250.00, 15.00, 360.00, 1, 10.42,4.58, 110.00),
('P013', 'Peanuts', 36, 190.00, 8.00, 288.00, 1, 5.28, 2.72, 98.00),
('P014', 'Popcorn', 12, 87.00, 15.00, 180.00, 0, 7.25, 7.75, 93.00),
('P015', 'Toppers', 12, 110.00, 15.00, 180.00, 0, 9.17, 5.83, 70.00);
GO

SELECT * FROM Products WHERE Quantity = 0

SELECT SUM(TotalProfit_ZAR) AS [Grand Total Profit (ZAR)] FROM Products;