import json
import csv
import os
import re

with open('toronto.csv', 'w') as datafile:
    fieldnames = ['Index', 'Name', 'Latitude', 'Longitude', 'NELong', 'NELat', 'SWLong', 'SWLat', 'Place ID', "hasBounds"]
    writer = csv.DictWriter(datafile, fieldnames=fieldnames)
    writer.writeheader()
    for file in os.listdir("loc_info"):
        if file.endswith(".json"):
            idx = re.findall("[-+]?\d+[\.]?\d*", file)[0]
            with open(str("loc_info/"+file)) as fh:
                data = json.load(fh)
                addr = data["formatted_address"]
                lat = data["geometry"]["location"]["lat"]
                lng = data["geometry"]["location"]["lng"]
                nelng = ""
                nelat = ""
                swlng = ""
                swlat = ""
                hasbounds = 0
                placeId = data["place_id"]
                if 'bounds' in data["geometry"].keys():
                    nelng = data["geometry"]["bounds"]["northeast"]["lng"],
                    nelat = data["geometry"]["bounds"]["northeast"]["lat"],
                    swlng = data["geometry"]["bounds"]["southwest"]["lng"],
                    swlat = data["geometry"]["bounds"]["southwest"]["lat"],
                    hasbounds = 1

                writer.writerow({'Index': idx,
                                 'Name': addr,
                                 'Latitude': lat,
                                 'Longitude': lng,
                                 'NELong': nelng,
                                 'NELat': nelat,
                                 'SWLong': swlng,
                                 'SWLat': swlat,
                                 'Place ID': placeId,
                                 'hasBounds': hasbounds})
