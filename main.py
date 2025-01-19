"""Weather flet app"""
from flet import *
import requests
import datetime

api_key = "06991f5a417d4300814113707251901"

url =f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=toronto&aqi=yes"
resp = requests.get(url)
data = resp.json()
print(data)