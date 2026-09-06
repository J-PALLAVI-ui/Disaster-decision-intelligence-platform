import pandas as pd
from sklearn.model_selection import train_test_split

# =====================================================
# Load Dataset
# =====================================================
print("=" * 60)
print("Loading Dataset...")

df = pd.read_csv("ml/data/training_dataset.csv")

print("Dataset Loaded Successfully!")
print(f"Total Records : {len(df)}")

# =====================================================
# Create Risk Labels using Quantiles
# =====================================================
print("\nCreating Risk Labels...")

df["risk"] = pd.qcut(
    df["magnitude"],
    q=3,
    labels=["Low", "Medium", "High"]
)

# =====================================================
# Select Features
# =====================================================
features = [
    "latitude",
    "longitude",
    "depth",
    "magnitude",
    "temperature",
    "humidity"
]

X = df[features]
y = df["risk"]

# =====================================================
# Train Test Split
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================================
# Display Dataset Information
# =====================================================
print("\n" + "=" * 60)
print("TRAINING INFORMATION")

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

print("\nFeatures Used")
print(features)

print("\nTarget Distribution")
print(y.value_counts())

print("\nFirst 10 Records")

print(
    df[
        [
            "magnitude",
            "risk"
        ]
    ].head(10)
)

# =====================================================
# Save Processed Dataset
# =====================================================
df.to_csv(
    "ml/data/preprocessed_dataset.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")
print("Location : ml/data/preprocessed_dataset.csv")