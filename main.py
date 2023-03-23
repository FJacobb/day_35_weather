import os

from twilio.rest import Client
import requests

TOKEN= os.environ.get("TOKEN")
SID = os.environ.get("SID")
API_KEY= os.environ.get("KEY")
CITY= "Niger, Nigeria"

minna_lon = 6.560457
minna_ltd = 9.588185
abuja_lon = 7.375315
abuja_ltd = 9.143305

API = "http://api.openweathermap.org/data/2.5/forecast"
PAREMETER = {
"lat":minna_ltd,
"lon":minna_lon,
"exclude":"current,minutely,daily",
"appid":API_KEY
}
MY_EMAIL = 'projectfestus@gmail.com'
sender_pass = 'iyfikarcqyergruh'

response = requests.get(url=API,params=PAREMETER)
response.raise_for_status()

weather_data = response.json()["list"]

datas=weather_data[:12]
data_id = [id['weather'][0] for id in datas]
x=700
rain = False
for data in data_id:
    if data["id"]<= 700:
        print(data["id"])
        duc = data['description']
        rain= True

os.system("python3 day_32_smtp/main.py")
if rain:
    client = Client(SID, TOKEN)
    message = client.messages.create(body=f"TODAY  WILL BE ({duc}). REMEMBER TO BRING AN ☂️☂️ ", from_="+14067307657", to="+2347040326271")
    print(message.status)

