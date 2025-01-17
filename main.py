import requests
import datetime as dt

MAR_VISTA_LAT = 34.019455
MAR_VISTA_LONG = -118.491188

### Learning how to use API to get JSON data ###
# print(response) # This gives back an HTTP [response code]
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # Uses Request module to raise errors for us
json_data = response.json()
iss_longitude = float(json_data["iss_position"]["longitude"])
iss_latitude = float(json_data["iss_position"]["latitude"])
# iss_position = (longitude, latitude)

# Your position is within +-5 degrees of the ISS position

parameters = {
    "lat": MAR_VISTA_LAT,
    "lng": MAR_VISTA_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Send me an email to tell me to look up
# BONUS: Run the code every 60 seconds

