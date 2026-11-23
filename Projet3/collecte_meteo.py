import os
from urllib import response
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
if api_key :
    print("API key loaded successfully.")
else:
    print("API key not found. Please check your .env file.")

params = {
    "q": "Paris",
    "appid": api_key,
    "units": "metric",
    "lang": "fr"
}

request = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
if request.status_code == 200:
    data = request.json()
    print(data)