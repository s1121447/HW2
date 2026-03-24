import requests
import json
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast?latitude=25.05&longitude=121.53&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
data = response.json()

output = {
    "city": "Taipei",
    "fetch_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "temperature_2m": data["current"]["temperature_2m"],
    "relative_humidity_2m": data["current"]["relative_humidity_2m"],
    "wind_speed_10m": data["current"]["wind_speed_10m"]
}

with open("weather.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("資料已成功存成 weather.json")