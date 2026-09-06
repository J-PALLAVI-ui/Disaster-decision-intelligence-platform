import pandas as pd

FILE_PATH = "data/processed/earthquakes_processed.csv"

df = pd.read_csv(FILE_PATH)

print("=" * 60)
print("EARTHQUAKE DATA VALIDATION")
print("=" * 60)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# Data types
print("\nData Types")
print(df.dtypes)

# Negative magnitude check
negative_mag = df[df["magnitude"] < 0]

print(f"\nNegative Magnitudes : {len(negative_mag)}")

# Depth check
negative_depth = df[df["depth"] < 0]

print(f"Negative Depths : {len(negative_depth)}")

print("\nValidation Completed Successfully")