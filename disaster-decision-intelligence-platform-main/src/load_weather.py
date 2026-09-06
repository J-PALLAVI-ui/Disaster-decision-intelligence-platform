import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:aks%40123@localhost:5432/disaster_decision_intelligence"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("data/raw/weather.csv")

df.to_sql(
    "weather",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Weather data loaded successfully!")
print(f"Rows Loaded: {len(df)}")