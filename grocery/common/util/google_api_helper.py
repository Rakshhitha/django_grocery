import requests
import datetime

from common.config.config import ConfigSectionMap


google_key = ConfigSectionMap("google")["api_key"]


def get_latitutde_longitude_from_pincode(pincode):
    api_key = google_key
    places_param = {"key": api_key, "address": pincode}
    places_list = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json", params=places_param
    )
    places_list = places_list.json()
    if len(places_list["results"]):
        location = places_list["results"][0]["geometry"]["location"]
        return location
    else:
        location = "Invalid Pincode entered."
        return location


def get_distance(source, destination):
    api_key = google_key
    now = datetime.datetime.now()
    time_stamp = int(now.timestamp()) + 3600
    query_params = {
        "key": api_key,
        "origin": source,
        "destination": destination,
        "departure_time": time_stamp,
        "mode": "driving",
    }
    direction_list = requests.get(
        "https://maps.googleapis.com/maps/api/directions/json", params=query_params
    )
    direction_list = direction_list.json()
    value = direction_list["routes"][0]["legs"][0]["distance"]["value"]
    return value
