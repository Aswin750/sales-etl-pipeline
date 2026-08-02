USE retail_sales;

CREATE TABLE IF NOT EXISTS sales (

    Order_ID VARCHAR(20) PRIMARY KEY,

    Order_Date DATE,

    Customer_ID VARCHAR(20),

    Customer_Name VARCHAR(100),

    City VARCHAR(50),

    Product VARCHAR(100),

    Category VARCHAR(50),

    Quantity INT,

    Unit_Price DECIMAL(10,2),

    Discount INT,

    Payment_Method VARCHAR(30),

    Order_Status VARCHAR(30),

    Sales DECIMAL(10,2)

);