import googlemaps
import csv
import json

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='AIzaSyD_A0so8ksE6PcZgD_cH66o-d_K_NUd_po')

with open('toronto-neighbourhoods.csv', 'rb') as neighbourhoods:
    reader = csv.reader(neighbourhoods)
    i = 0
    for row in reader:
        loc_name = row[0]+ ", Toronto, Canada"
        geocode_result = gmaps.geocode(loc_name)
        if len(geocode_result) > 0:
            file_name = "loc_info/" + str(i) + "-info.json"
            i += 1
            result = geocode_result[0]
            with open(file_name, 'w') as fp:
                json.dump(result, fp)
        else:
            with open('failed-neighbourhoods.txt', 'w') as fail_file:
                fail_file.write(row[0])
                fail_file.write("\n")
