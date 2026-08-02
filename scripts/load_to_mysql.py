import mysql.connector
import pandas as pd


connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="aswin@4863",
    database="retail_sales"

)
print("Connected successfully")

cursor = connection.cursor()

print("Cursor Created Successfully!")

cursor.execute("SELECT DATABASE();")

result = cursor.fetchone()

print(result)

df = pd.read_csv("data/cleaned/sales_clean.csv")

insert_query = """
INSERT INTO sales (
    Order_ID,
    Order_Date,
    Customer_ID,
    Customer_Name,
    City,
    Product,
    Category,
    Quantity,
    Unit_Price,
    Discount,
    Payment_Method,
    Order_Status,
    Sales
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (
        row["Order_ID"],
        row["Order_Date"],
        row["Customer_ID"],
        row["Customer_Name"],
        row["City"],
        row["Product"],
        row["Category"],
        row["Quantity"],
        row["Unit_Price"],
        row["Discount"],
        row["Payment_Method"],
        row["Order_Status"],
        row["Sales"]
    ))

connection.commit()
cursor.close()
connection.close()