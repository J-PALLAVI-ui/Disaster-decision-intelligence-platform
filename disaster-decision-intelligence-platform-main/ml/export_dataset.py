import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:aks%40123@localhost:5432/disaster_decision_intelligence"

engine = create_engine(DATABASE_URL)

query = """
SELECT
    e.id,
    e.date,
    e.time,
    e.place,
    e.latitude,
    e.longitude,
    e.depth,
    e.magnitude,
    e.tsunami,
    w.temperature,
    w.humidity,
    w.description
FROM earthquakes e
INNER JOIN weather w
ON e.id = w.earthquake_id;
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)

df.to_csv("ml/data/training_dataset.csv", index=False)

print("✅ Dataset exported successfully!")