import pandas as pd

df=pd.read_csv("data/sales_raw_dirty.csv")

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)

print("\n"+"=" * 60 )
print("Dataset information")
print("=" * 60)
print(df.info())

print("\n"+"-" * 60)
print("Numerical summary")
print(df.describe())

print("\n"+"-" * 60)
print("Missing values")
print(df.isnull().sum())

print("\n"+"-" * 60)
print("Dupicate values")
print(df.duplicated().sum())

print("\n"+"-" * 60)
print("First 5 raws")
print(df.head())