import pandas as pd
import os

print("SCRIPT STARTED")

# -----------------------------
# Load raw data
# -----------------------------
df = pd.read_csv("data/raw_sales_data.csv")

print("RAW DATA LOADED")
print(df.head())

# -----------------------------
# Standardize column names
# -----------------------------
df.columns = df.columns.str.lower()

print("COLUMNS AFTER STANDARDIZATION:", df.columns.tolist())

# -----------------------------
# Handle missing values
# -----------------------------
df["product"].fillna("Unknown", inplace=True)
df["price"].fillna(df["price"].median(), inplace=True)
df["quantity"].fillna(1, inplace=True)
df["city"].fillna("Unknown", inplace=True)

# -----------------------------
# Fix text inconsistency
# -----------------------------
df["city"] = df["city"].str.title()
df["category"] = df["category"].str.title()

# -----------------------------
# Convert date column
# -----------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# -----------------------------
# Create new feature
# -----------------------------
df["total_sales"] = df["price"] * df["quantity"]

print("TOTAL_SALES CREATED")
print(df[["city", "price", "quantity", "total_sales"]].head())

# -----------------------------
# Ensure output directory exists
# -----------------------------
os.makedirs("output", exist_ok=True)

# -----------------------------
# Save cleaned data
# -----------------------------
df.to_csv("data/cleaned_sales_data.csv", index=False)
print("CLEANED DATA SAVED")

# -----------------------------
# Analysis: Sales by city
# -----------------------------
sales_by_city = df.groupby("city")["total_sales"].sum()

print("GROUPBY RESULT:")
print(sales_by_city)

# -----------------------------
# Save analysis output
# -----------------------------
sales_by_city.to_csv("output/analysis_summary.csv")
print("ANALYSIS SUMMARY SAVED")

print("SCRIPT COMPLETED SUCCESSFULLY")

