import pandas as pd

# Read CSV file
df = pd.read_csv("sales_data.csv", encoding="latin1")



print("Rows and columns before cleaning:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Drop rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove invalid quantity and price
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Create new columns
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["OrderDate"] = df["InvoiceDate"].dt.date
df["OrderMonth"] = df["InvoiceDate"].dt.month
df["OrderYear"] = df["InvoiceDate"].dt.year

print("Rows and columns after cleaning:", df.shape)

# Save cleaned data
df.to_csv("sales_cleaned.csv", index=False)

print("Task 1 completed successfully")