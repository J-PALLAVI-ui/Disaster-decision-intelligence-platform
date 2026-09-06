import os
import requests
import pandas as pd

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
    "all_day.geojson"
)

OUTPUT_FILE = "data/raw/earthquakes.csv"


def fetch_earthquake_data():

    print("Downloading earthquake data...")

    response = requests.get(USGS_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    earthquakes = []

    for feature in data["features"]:

        properties = feature["properties"]
        geometry = feature["geometry"]

        earthquakes.append({
            "id": feature["id"],
            "magnitude": properties["mag"],
            "place": properties["place"],
            "time": properties["time"],
            "updated": properties["updated"],
            "status": properties["status"],
            "tsunami": properties["tsunami"],
            "longitude": geometry["coordinates"][0],
            "latitude": geometry["coordinates"][1],
            "depth": geometry["coordinates"][2]
        })

    return pd.DataFrame(earthquakes)


def save_raw_data(df):

    os.makedirs("data/raw", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nData saved successfully!")

    print(f"Location : {OUTPUT_FILE}")

    print(f"Records  : {len(df)}")


if __name__ == "__main__":

    df = fetch_earthquake_data()

    print(df.head())

    save_raw_data(df)