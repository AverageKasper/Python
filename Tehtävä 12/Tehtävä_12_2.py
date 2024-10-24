import requests
import json

api = "d1187dec0bdb32d1a030a27b739d24a2"
city_name = input("What city are you intrested?\n")

try:
    weather_request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}"
    weather_result = requests.get(weather_request).json()
    weather_description = weather_result["weather"][0]["description"]
    weather_degree_k = weather_result["main"]["temp"]
    weather_degree_c = weather_degree_k - 273.15
    name = weather_result["name"]
    print(f"At {name}, Weather looks like {weather_description} and its {weather_degree_c:.2f} celcius!")
except requests.exceptions.RequestException as e:
    print("Could not complete request")