# 🚀 Retail Sales ETL Pipeline

An end-to-end Retail Sales ETL (Extract, Transform, Load) pipeline built using **Python, Pandas, MySQL, SQL, Power BI, Git, and GitHub**.

This project demonstrates the complete data engineering workflow—from generating raw sales data to cleaning, transforming, loading it into a relational database, and creating an interactive business intelligence dashboard.

---

## 📌 Project Overview

The objective of this project is to simulate a real-world retail sales data pipeline by performing the following tasks:

- Generate retail sales data
- Introduce real-world data quality issues
- Clean and transform the dataset using Python
- Load the processed data into MySQL
- Perform SQL-based business analysis
- Build an interactive Power BI dashboard
- Manage source code using Git and GitHub

---

# 🏗️ Project Architecture

```text
                    Raw Sales Dataset
                           │
                           ▼
                 Data Cleaning (Pandas)
                           │
                           ▼
               Transformed Clean Dataset
                           │
                           ▼
               Load into MySQL Database
                           │
                           ▼
                  SQL Business Analysis
                           │
                           ▼
             Power BI Interactive Dashboard
```

---

# 🔄 ETL Workflow

### Extract
- Generated retail sales dataset using Python.
- Simulated realistic sales transactions.

### Transform
Performed data cleaning using Pandas:
- Removed duplicate records
- Handled missing values
- Standardized city names
- Corrected inconsistent text formatting
- Fixed data types
- Calculated Sales Amount

### Load
- Connected Python with MySQL
- Created database tables
- Loaded cleaned data into MySQL

### Analyze
Performed SQL analysis including:
- Revenue by Category
- Revenue by City
- Top Customers
- Payment Method Distribution
- Sales Trend Analysis

### Visualize
Designed an interactive Power BI dashboard with:
- KPI Cards
- Revenue Trends
- Category Analysis
- City-wise Sales
- Top Customers
- Interactive Slicers

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | MySQL |
| Query Language | SQL |
| Visualization | Power BI |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 📂 Project Structure

```text
sales-etl-pipeline/
│
├── dashboard/
│   └── Retail_Sales_Dashboard.pbix
│
├── data/
│   ├── raw_sales.csv
│   └── cleaned_sales.csv
│
├── notebooks/
│
├── screenshots/
│   ├── dashboard_overview.png
│   └── dashboard_kpi.png
│
├── scripts/
│   ├── generate_dataset.py
│   ├── clean_dataset.py
│   └── load_to_mysql.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🗄 Database Schema

## Customers

| Column |
|--------|
| CustID |
| CustName |
| OrderID |
| City |

---

## Products

| Column |
|--------|
| OrderID |
| Product |
| Category |
| Quantity |
| UnitPrice |

---

## Sales

| Column |
|--------|
| OrderID |
| CustID |
| City |
| Product |
| Quantity |
| UnitPrice |
| Discount |
| PaymentMethod |

---

# 📊 Power BI Dashboard

## Dashboard Preview

> Add your dashboard screenshot below.

```markdown
![Dashboard](screenshots/dashboard_overview.png)
```

---

## Dashboard Features

✔ Revenue KPI

✔ Total Orders

✔ Total Customers

✔ Category-wise Sales

✔ Top Customers

✔ Revenue Trend

✔ City-wise Performance

✔ Payment Method Analysis

✔ Interactive Filters

---

# 📈 Sample Business Insights

The dashboard helps answer questions such as:

- Which category generates the highest revenue?
- Which city contributes the most sales?
- Who are the top customers?
- Which payment method is most popular?
- What are the monthly sales trends?

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/Aswin750/sales-etl-pipeline.git
```

---

## 2. Navigate to Project

```bash
cd sales-etl-pipeline
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate Dataset

```bash
python scripts/generate_dataset.py
```

---

## 5. Clean Dataset

```bash
python scripts/clean_dataset.py
```

---

## 6. Load into MySQL

```bash
python scripts/load_to_mysql.py
```

---

## 7. Execute SQL Analysis

Run the SQL scripts available in the `sql/` folder.

---

## 8. Open Dashboard

Open:

```
dashboard/Retail_Sales_Dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# 🎯 Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- Data Cleaning
- Data Transformation
- SQL Query Writing
- Database Design
- MySQL Integration
- Business Intelligence
- Power BI Dashboard Design
- Git Version Control
- GitHub Project Management

---

# 📌 Future Improvements

- Automate the ETL pipeline using Apache Airflow
- Store data in AWS S3
- Load data into Amazon RDS
- Add logging and error handling
- Containerize the project using Docker
- Build a Streamlit web interface
- Schedule automated pipeline execution

---

