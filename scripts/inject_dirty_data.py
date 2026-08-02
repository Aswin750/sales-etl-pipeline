import pandas as pd
import random

# Read the clean dataset
df = pd.read_csv("data/sales_raw.csv")

# -----------------------------
# 1. Extra spaces in Customer_Name (5%)
# -----------------------------
for index in df.sample(frac=0.05, random_state=1).index:
    df.loc[index, "Customer_Name"] = " " + str(df.loc[index, "Customer_Name"]) + " "

# -----------------------------
# 2. Mixed Case in Payment_Method (5%)
# -----------------------------
for index in df.sample(frac=0.05, random_state=2).index:

    value = df.loc[index, "Payment_Method"]

    choice = random.choice(["lower", "upper", "title"])

    if choice == "lower":
        df.loc[index, "Payment_Method"] = value.lower()

    elif choice == "upper":
        df.loc[index, "Payment_Method"] = value.upper()

    else:
        df.loc[index, "Payment_Method"] = value.title()

# -----------------------------
# 3. Missing Customer Names (3%)
# -----------------------------
for index in df.sample(frac=0.03, random_state=3).index:
    df.loc[index, "Customer_Name"] = None

# -----------------------------
# 4. Missing Unit Price (2%)
# -----------------------------
for index in df.sample(frac=0.02, random_state=4).index:
    df.loc[index, "Unit_Price"] = None

# -----------------------------
# 5. Negative Quantity (2%)
# -----------------------------
for index in df.sample(frac=0.02, random_state=5).index:
    df.loc[index, "Quantity"] = -random.randint(1,5)

# -----------------------------
# 6. Invalid Discount (>100) (2%)
# -----------------------------
for index in df.sample(frac=0.02, random_state=6).index:
    df.loc[index, "Discount"] = random.randint(110,150)

# -----------------------------
# 7. Duplicate Rows (3%)
# -----------------------------
duplicates = df.sample(frac=0.03, random_state=7)

df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle dataset
df = df.sample(frac=1, random_state=10).reset_index(drop=True)

# Save dirty dataset
df.to_csv("data/sales_raw_dirty.csv", index=False)

print("Dirty dataset created successfully!")

print(f"Total Records : {len(df)}")
print(df.head())