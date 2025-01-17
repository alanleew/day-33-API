import requests
import datetime as dt
import smtplib
import time

EMAIL = "100dopython@gmail.com"
PASSWORD = "plkkkflgqyxpntxx"
MAR_VISTA_LAT = 34.019455
MAR_VISTA_LONG = -118.491188

### Learning how to use API to get JSON data ###
def is_iss_overhead():
    # print(response) # This gives back an HTTP [response code]
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # Uses Request module to raise errors for us
    json_data = response.json()
    iss_latitude = float(json_data["iss_position"]["latitude"])
    iss_longitude = float(json_data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    # print(f"ISS position: {iss_position}")

    # Your position is within +-5 degrees of the ISS position
    # print(f"Our position: {MAR_VISTA_LAT, MAR_VISTA_LONG}")
    parameters = {
        "lat": MAR_VISTA_LAT,
        "lng": MAR_VISTA_LONG,
        "formatted": 0
    }
    if abs(iss_latitude-MAR_VISTA_LAT) <= 5 and abs(iss_longitude-MAR_VISTA_LONG) <= 5:
        return True

def is_nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(f"Mar Vista sunrise hour: {sunrise}\nMar Vista sunset hour: {sunset}")
    current = (dt.datetime.now().hour + 8) % 24
    # print(f"Mar Vista hour: {current}")

    # if (sunset < current < sunrise) or (current < sunrise < sunset) or (sunrise < sunset < current):
    #     print("It's nighttime")
    # else:
    #     print("It's daytime")

    if (sunset < current < sunrise) or (current < sunrise < sunset) or (sunrise < sunset < current):
        return True

while True:
    time.sleep(60) # Allows us to run every 60 seconds
    if is_iss_overhead() and is_nighttime():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()  # Encrypts message
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="dopython@yahoo.com",
            msg=f"Subject: LOOK UP!\n\nISS is right above us, look up in the sky!"
        )
