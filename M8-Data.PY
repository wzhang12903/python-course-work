import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv("sales.csv")

print("Dataset Preview:")
print(df.head())

print("\nShape of dataset:", df.shape)

# Data Cleaning

# Check missing values
print("\nMissing values:")
print("\nMissing values:")
for col, val in df.isnull().sum().items():
    print(f"{col}: {val}")

# Remove duplicates (if any)
df = df.drop_duplicates()

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Data Analysis


# 1. Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# 2. Average sales
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# Group by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
for category, value in category_sales.items():
    print(f"{category}: {value}")

# Visualization 1: Bar Chart

category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Visualization 2: Line Chart

daily_sales = df.groupby("Date")["Sales"].sum()

daily_sales.plot(kind="line")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
