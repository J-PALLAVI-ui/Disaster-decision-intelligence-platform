import os
import joblib
import pandas as pd

# =====================================================
# Load Trained Model
# =====================================================

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "ml",
    "models",
    "best_model.pkl"
)

model = joblib.load(MODEL_PATH)

# =====================================================
# Prediction Function
# =====================================================

def predict_magnitude(latitude, longitude, depth, temperature, humidity):
    """
    Predict earthquake magnitude using the trained model.
    """

    features = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "depth": depth,
        "temperature": temperature,
        "humidity": humidity
    }])

    prediction = model.predict(features)[0]

    return float(prediction)