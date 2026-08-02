import random
import pandas as pd
from datetime import datetime, timedelta

products = {
    "Laptop": ("Electronics", 55000),
    "Smartphone": ("Electronics", 30000),
    "Headphones": ("Accessories", 2500),
    "Keyboard": ("Accessories", 1500),
    "Monitor": ("Electronics", 12000),
    "Printer": ("Electronics", 8000),
    "Mouse": ("Accessories", 700),
    "Smartwatch": ("Wearables", 5000)
}

cities = [
    "Kochi",
    "Bengaluru",
    "Chennai",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune",
    "Coimbatore"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

statuses = [
    "Delivered",
    "Cancelled",
    "Returned"
]

customer_names = [
    "Rahul Sharma",
    "Priya Nair",
    "Arjun Menon",
    "Sneha Reddy",
    "Anjali Menon",
    "Vikram Singh",
    "Neha Kapoor",
    "Amit Kumar",
    "Sanjay Das",
    "Meera Iyer"
]

def generate_order_id(number):
    return f"ORD{number:06d}"

def generate_order_date():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    days_between = (end_date - start_date).days

    random_days = random.randint(0, days_between)

    order_date = start_date + timedelta(days=random_days)

    return order_date.strftime("%Y-%m-%d")

def generate_customer(customer_number):
    customer_id=f"CUST{customer_number:06d}"
    customer_name=random.choice(customer_names)
    return customer_id,customer_name


def generate_product():
    product=random.choice(list(products.keys()))
    category,unit_price=products[product]
    return product,category,unit_price


def generate_city():
    return random.choice(cities)


def generate_quantity():
    return random.randint(1,5)


def generate_discount():
    discounts=[5,10,15,20,15,30]
    return random.choice(discounts)


def generate_payment_method():
    return random.choice(payment_methods)


def generate_order_status():
    return random.choice(statuses)


records=[]

for i in range(1,1001):
    order_id=generate_order_id(i)
    order_date=generate_order_date()
    customer_id,customer_name=generate_customer(i)
    product,category,unit_price=generate_product()
    city=generate_city()
    quantity=generate_quantity()
    discount=generate_discount()
    payment_method=generate_payment_method()
    order_status=generate_order_status()
    sales = quantity * unit_price * (1 - discount / 100)
    record = {
        "Order_ID": order_id,
        "Order_Date":order_date,
        "Customer_ID": customer_id,
        "Customer_Name": customer_name,
        "City": city,
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Discount": discount,
        "Payment_Method": payment_method,
        "Order_Status": order_status,
        "Sales": round(sales, 2)
    }
    records.append(record)
df=pd.DataFrame(records)
print(df.head())
df.to_csv("data/sales_raw.csv", index=False)

print("\nDataset generated successfully!")
print(f"Total Records: {len(df)}")