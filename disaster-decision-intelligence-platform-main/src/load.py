import pandas as pd
from sqlalchemy import create_engine

# -----------------------
# Database Connection
# -----------------------

DATABASE_URL = "postgresql://postgres:aks%40123@postgres:5432/disaster_decision_intelligence"

engine = create_engine(DATABASE_URL)

# -----------------------
# Read Processed CSV
# -----------------------

df = pd.read_csv("data/processed/earthquakes_processed.csv")

# -----------------------
# Load into PostgreSQL
# -----------------------

df.to_sql(
    "earthquakes",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Earthquake data loaded successfully!")
print(f"Rows Loaded: {len(df)}")