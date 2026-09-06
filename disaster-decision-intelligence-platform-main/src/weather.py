import requests
import pandas as pd

API_KEY = "04af1e4088ea99f5f928cfe53897c0f8"

LAT = 35.6895
LON = 139.6917

url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code != 200:
    print("Error:", response.json())
    exit()

data = response.json()

weather = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "wind_speed": data["wind"]["speed"],
    "weather": data["weather"][0]["main"],
    "description": data["weather"][0]["description"],
    "latitude": data["coord"]["lat"],
    "longitude": data["coord"]["lon"]
}

df = pd.DataFrame([weather])

print(df)

df.to_csv("data/raw/weather.csv", index=False)

print("\n✅ Weather data saved successfully!")