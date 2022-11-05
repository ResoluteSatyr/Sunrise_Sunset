import requests
from datetime import datetime
import time
LATITUDE = 39.739235
LONGITUDE = -104.990250

# Creating Satellite variables
satellite = requests.get(url="http://api.open-notify.org/iss-now.json")
satellite.raise_for_status()
data_from_satellite = satellite.json()
lat_from_sat = float(data_from_satellite["iss_position"]["latitude"])
lon_from_sat = float(data_from_satellite["iss_position"]["longitude"])


# Setting the parameter formatted to 0 returns the time in the 24 hrs format
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "formatted": 0
}
# Creating Sunrise and Sunset variables
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

# Current time variable
time_now = datetime.now()


"""Check if ISS Satellite is near my location"""
CHECK_DISTANCE = float(5)


def is_satellite_near():
    f = CHECK_DISTANCE
    if time_now.hour > int(sunset) or time_now.hour < int(sunrise):
        if LATITUDE-5 <= lat_from_sat <= LATITUDE+5 and LONGITUDE-5 <= lon_from_sat <= LONGITUDE+5:
            print("Is overhead")
    else:
        print("not yet")


# Scans Satellite position every 60 seconds
scanning = True
while scanning:
    time.sleep(60)
    is_satellite_near()
