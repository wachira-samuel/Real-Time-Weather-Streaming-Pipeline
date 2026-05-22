import requests
import json
import time
from kafka import KafkaProducer

API_KEY = "YOUR_OPENWEATHER_API_KEY"
CITY = "Nairobi"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

while True:
    data = get_weather()

    weather_event = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "timestamp": data["dt"]
    }

    producer.send("weather-data", weather_event)
    print("Sent:", weather_event)

    time.sleep(10)