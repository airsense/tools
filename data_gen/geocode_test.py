import googlemaps
import json

gmaps = googlemaps.Client(key='AIzaSyD_A0so8ksE6PcZgD_cH66o-d_K_NUd_po')

# Geocoding an address
geocode_result = gmaps.geocode('Toronto, Ontario, Canada')

result = geocode_result[0]
formatted_address = result['formatted_address']
geometry = result['geometry']
location = geometry['location']
lat = location['lat']
lng = location['lng']

with open('loc_info/result.json', 'w') as fp:
    json.dump(result, fp)

print lat
print lng
