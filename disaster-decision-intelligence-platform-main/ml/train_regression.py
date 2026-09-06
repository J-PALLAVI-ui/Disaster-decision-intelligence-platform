import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading Dataset...")

df = pd.read_csv("ml/data/preprocessed_dataset.csv")

# =====================================================
# Features
# =====================================================

X = df[
    [
        "latitude",
        "longitude",
        "depth",
        "temperature",
        "humidity"
    ]
]

# =====================================================
# Target
# =====================================================

y = df["magnitude"]

# =====================================================
# Train/Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =====================================================
# Models
# =====================================================

models = {

    "Random Forest":
        RandomForestRegressor(
            random_state=42
        ),

    "XGBoost":
        XGBRegressor(
            random_state=42
        ),

    "CatBoost":
        CatBoostRegressor(
            verbose=False,
            random_state=42
        ),

    "LightGBM":
        LGBMRegressor(
            random_state=42
        )

}

results = []

best_model = None
best_r2 = -999

# =====================================================
# Training
# =====================================================

for name, model in models.items():

    print("\n" + "=" * 60)
    print(f"Training {name}")

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)

    rmse = mean_squared_error(
        y_test,
        pred
    ) ** 0.5

    r2 = r2_score(
        y_test,
        pred
    )

    results.append(
        [
            name,
            mae,
            rmse,
            r2
        ]
    )

    if r2 > best_r2:

        best_r2 = r2
        best_model = model

# =====================================================
# Results
# =====================================================

results_df = pd.DataFrame(

    results,

    columns=[
        "Model",
        "MAE",
        "RMSE",
        "R2 Score"
    ]

)

print("\n")
print(results_df)

results_df.to_csv(
    "ml/data/regression_results.csv",
    index=False
)

joblib.dump(
    best_model,
    "ml/models/best_model.pkl"
)

print("\nBest Regression Model Saved!")