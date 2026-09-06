from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import text
import traceback

from src.database import engine
from src.decision_engine import DecisionEngine
from src.predictor import predict_magnitude

app = FastAPI(
    title="Disaster Decision Intelligence Platform",
    version="2.0"
)

# ======================================================
# Request Model
# ======================================================

class EarthquakeRequest(BaseModel):
    latitude: float
    longitude: float
    depth: float
    temperature: float
    humidity: float


# ======================================================
# Home
# ======================================================

@app.get("/")
def home():

    return {
        "message": "Disaster Decision Intelligence Platform API Running"
    }


# ======================================================
# AI Prediction
# ======================================================

@app.post("/predict")
def predict(data: EarthquakeRequest):

    # Predict earthquake magnitude using ML model
    predicted_magnitude = predict_magnitude(
        latitude=data.latitude,
        longitude=data.longitude,
        depth=data.depth,
        temperature=data.temperature,
        humidity=data.humidity
    )

    # Decision Intelligence
    decision = DecisionEngine.analyze(
        magnitude=predicted_magnitude,
        depth=data.depth,
        temperature=data.temperature,
        humidity=data.humidity
    )

    return {

        "input": {

            "latitude": data.latitude,
            "longitude": data.longitude,
            "depth": data.depth,
            "temperature": data.temperature,
            "humidity": data.humidity

        },

        "predicted_magnitude": round(predicted_magnitude, 2),

        "decision": decision

    }


# ======================================================
# Latest Earthquake
# ======================================================

@app.get("/latest-earthquake")
def latest_earthquake():

    try:

        sql = text("""
        SELECT
            e.place,
            e.latitude,
            e.longitude,
            e.magnitude,
            e.depth,
            w.temperature,
            w.humidity
        FROM earthquakes e
        INNER JOIN weather w
            ON e.id = w.earthquake_id
        ORDER BY e.time DESC
        LIMIT 1
        """)

        with engine.connect() as conn:

            result = conn.execute(sql)
            row = result.fetchone()

        if row is None:

            return {
                "message": "No earthquake data found."
            }

        # ML Prediction
        predicted_magnitude = predict_magnitude(
            latitude=float(row.latitude),
            longitude=float(row.longitude),
            depth=float(row.depth),
            temperature=float(row.temperature),
            humidity=float(row.humidity)
        )

        # Decision Engine
        decision = DecisionEngine.analyze(
            magnitude=predicted_magnitude,
            depth=float(row.depth),
            temperature=float(row.temperature),
            humidity=float(row.humidity)
        )

        return {

            "earthquake": {

                "place": row.place,
                "latitude": row.latitude,
                "longitude": row.longitude,
                "actual_magnitude": row.magnitude,
                "predicted_magnitude": round(predicted_magnitude, 2),
                "depth": row.depth,
                "temperature": row.temperature,
                "humidity": row.humidity

            },

            "decision": decision

        }

    except Exception as e:

        traceback.print_exc()

        return {

            "error": str(e)

        }


# ======================================================
# Health Check
# ======================================================

@app.get("/health")
def health():

    return {

        "status": "healthy",
        "service": "Disaster Decision Intelligence Platform",
        "database": "connected",
        "ml_model": "loaded"

    }