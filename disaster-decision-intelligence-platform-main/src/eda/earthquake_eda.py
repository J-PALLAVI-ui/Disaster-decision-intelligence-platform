import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/earthquakes.csv")

plt.figure(figsize=(8,5))

plt.hist(df["magnitude"].dropna(), bins=20)

plt.title("Earthquake Magnitude Distribution")

plt.xlabel("Magnitude")

plt.ylabel("Count")

plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/earthquakes.csv")

# -----------------------------
# 1. Magnitude Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["magnitude"].dropna(), bins=20)
plt.title("Earthquake Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# -----------------------------
# 2. Depth Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["depth"].dropna(), bins=20)
plt.title("Earthquake Depth Distribution")
plt.xlabel("Depth (km)")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# -----------------------------
# 3. Magnitude vs Depth
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["magnitude"], df["depth"])
plt.title("Magnitude vs Depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth (km)")
plt.grid(True)
plt.show()

# -----------------------------
# 4. Tsunami Counts
# -----------------------------
plt.figure(figsize=(6,4))
df["tsunami"].value_counts().plot(kind="bar")
plt.title("Tsunami Flag")
plt.xlabel("Tsunami")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 5. Top 10 Earthquake Locations
# -----------------------------
plt.figure(figsize=(10,5))
df["place"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Earthquake Locations")
plt.xlabel("Location")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()