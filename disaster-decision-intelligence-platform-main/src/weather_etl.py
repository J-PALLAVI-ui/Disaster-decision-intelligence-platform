import pandas as pd
import requests
import time

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Read earthquake data
earthquakes = pd.read_csv("data/processed/earthquakes_processed.csv")

# Take only first 10 records

weather_data = []

for _, row in earthquakes.iterrows():

    lat = row["latitude"]
    lon = row["longitude"]

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        weather_data.append({

            "earthquake_id": row["id"],
            "place": row["place"],
            "latitude": lat,
            "longitude": lon,
            "magnitude": row["magnitude"],

            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"]

        })

        print(f"Downloaded weather for {row['place']}")

    else:

        print(f"Failed: {row['place']}")

    time.sleep(1)

weather_df = pd.DataFrame(weather_data)

weather_df.to_csv("data/raw/weather.csv", index=False)

print("\nWeather ETL Completed!")
print(weather_df.head())