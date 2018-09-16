import requests
import urllib.parse


def geocode(map_obj=None):
    error_msg = "Object not found!"
    map_object_encoded = urllib.parse.quote(map_obj)
    url = 'https://nominatim.openstreetmap.org/search?q=' + \
          map_object_encoded + \
          '&format=json&polygon=0&addressdetails=0'
    try:
        request = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return
    json_response = request.json()
    # print(json_response)
    if not json_response or 'error' in json_response:
        # print(error_msg)
        return error_msg
    else:
        lat = round(float(json_response[0]["lat"]), 5)
        lon = round(float(json_response[0]["lon"]), 5)
        # print("Object: " + json_response[0]["display_name"])
        # print("Lat: " + str(lat), "Lon: " + str(lon))
        return lat, lon


def reverse(lat: float=0.0, lon: float=0.0):
    if not isinstance(lat, float) or not isinstance(lon, float):
        e = "Invalid input!"
        # print(e)
        return e
    else:
        error_msg = "Object not found!"
        url = 'https://nominatim.openstreetmap.org/reverse?format=json&' + \
              'lat=' + str(lat) + \
              '&' + \
              'lon=' + str(lon) + \
              '&zoom=18&addressdetails=0'
        try:
            request = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        json_response = request.json()
        # print(json_response)
        if not json_response or 'error' in json_response:
            # print(error_msg)
            return error_msg
        else:
            result = json_response["display_name"]
            # print(result)
            return result


def main():
    while True:
        try:
            option = int(input("Geocoding (1)\nReverse geocoding (2)\nEnter option: "))
            break
        except ValueError:
            print("That's not a valid option!\n")

    if option == 1:
        print("<Geocoding>")
        map_object = input('Enter the name of object (city, street, site, etc.): ')
        geocode(map_object)
    elif option == 2:
        print("<Reverse geocoding>")
        lat, lon = input("Enter lattitude and longitude divided by ',': ").split(",")
        reverse(lat, lon)
    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()


