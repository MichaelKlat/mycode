import time

import json

import urllib.request

import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Extract the ISS location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']
#time = location['timestamp']

# Ouput lon and lat to the terminal
lat = float(lat)
lon = float(lon)

coords_tuple= (lat, lon)

result1 = rg.search(coords_tuple)

ts= result['timestamp']

hr_ts= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

#print(result['timestamp'])
#print("Timestamp: " + str(time))
print("Timestamp: " + str(hr_ts))
print("iss_position: " + str(location)) 
print("\nLatitude: " + str(lat))
print("\nLongitude: " + str(lon))
print(result1[0]["name"])
print(result1[0]["cc"])
