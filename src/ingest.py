import requests
import json
from pathlib import Path

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
          "latitude": -25.7479,
        "longitude": 28.2293,
        "current": "temperature_2m,relative_humidity_2m",
    }
    response = requests.get(url,params=params,timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    weather = fetch_weather()
    current = weather["current"]
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"],"%")

    output_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "weather.json"

    with open(output_path,"w") as file:
        json.dump(weather,file,indent=4)
