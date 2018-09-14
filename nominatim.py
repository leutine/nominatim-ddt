import requests
import urllib.parse


def geocode():
    map_object = input('Ввод ')
    map_object_encoded = urllib.parse.quote(map_object)
    url = 'https://nominatim.openstreetmap.org/search?q=' + \
          map_object_encoded + \
          '&format=json&polygon=0&addressdetails=0'
    r = requests.get(url)
    json_response = r.json()
    lat = round(float(json_response[0]["lat"]), 5)
    lon = round(float(json_response[0]["lon"]), 5)
    print("Lat: " + str(lat), "Lon: " + str(lon))


geocode()
