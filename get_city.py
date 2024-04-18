import googlemaps
import os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")

def find_closest_city(latitude, longitude, api_key):
    gmaps = googlemaps.Client(key=api_key)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    
    for result in reverse_geocode_result:
        for component in result['address_components']:
            if 'locality' in component['types']:
                return component['long_name']


latitude = 50.9699
longitude = 0.4160

closest_city = find_closest_city(latitude, longitude, api_key)
print("Closest city:", closest_city)