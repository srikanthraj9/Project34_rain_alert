import requests
from twilio.rest import Client

account_sid = "ACf638a78a8b8e052a2b8971d6b6d62f5d"
auth_token = "bbb2c7d1ab629f3c64f5b1ff671e84c9"

own_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "002994f55316fb732f7fe7ba0dfb976e"

weather_params = {
    "lat": 23.022505,
    "lon": 72.571365,
    "appid": api_key ,
    "con":4 ,
}

response = requests.get(own_endpoint, params=weather_params)
response.raise_for_status()
whether_data = response.json()
# print(whether_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_weather in whether_data["list"]:
    conditions_code = hour_weather["weather"][0]["id"]
    if conditions_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="it's going to rain today .remember to bring an ☂️",
        from_="+18786887494",
        to="+91 80747 77427",
    )
    print(message.body)

