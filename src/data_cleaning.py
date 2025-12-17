import pandas as pd

# Load data
df = pd.read_csv("data/raw_sales_data.csv")

# Standardize column names
df.columns = df.columns.str.lower()

# Handle missing values
df["product"].fillna("Unknown", inplace=True)
df["price"].fillna(df["price"].median(), inplace=True)
df["quantity"].fillna(1, inplace=True)
df["city"].fillna("Unknown", inplace=True)

# Fix text inconsistency
df["city"] = df["city"].str.title()
df["category"] = df["category"].str.title()

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Create new feature
df["total_sales"] = df["price"] * df["quantity"]

# Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("Data cleaning completed successfully.")
