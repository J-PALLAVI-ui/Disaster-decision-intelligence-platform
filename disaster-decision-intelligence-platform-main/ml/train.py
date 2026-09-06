import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv("ml/data/preprocessed_dataset.csv")

# =====================================================
# Features
# =====================================================

X = df[
    [
        "latitude",
        "longitude",
        "depth",
        "magnitude",
        "temperature",
        "humidity"
    ]
]

# =====================================================
# Target
# =====================================================

y = df["risk"]

# Convert labels to numbers

mapping = {
    "Low":0,
    "Medium":1,
    "High":2
}

y = y.map(mapping)

# =====================================================
# Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================================
# Models
# =====================================================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(random_state=42),

    "XGBoost":
        XGBClassifier(
            eval_metric="mlogloss",
            random_state=42
        ),

    "CatBoost":
        CatBoostClassifier(
            verbose=False,
            random_state=42
        ),

    "LightGBM":
        LGBMClassifier(
            random_state=42
        )

}

results = []

best_model = None
best_accuracy = 0

# =====================================================
# Training
# =====================================================

for name, model in models.items():

    print("="*60)
    print(f"Training {name}")

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    accuracy = accuracy_score(y_test,pred)

    precision = precision_score(
        y_test,
        pred,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        pred,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        pred,
        average="weighted"
    )

    results.append(
        [
            name,
            accuracy,
            precision,
            recall,
            f1
        ]
    )

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model

# =====================================================
# Results
# =====================================================

results_df = pd.DataFrame(

    results,

    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]

)

print("\n")
print(results_df)

results_df.to_csv(
    "ml/data/model_results.csv",
    index=False
)

joblib.dump(
    best_model,
    "ml/models/best_model.pkl"
)

print("\nBest Model Saved!")