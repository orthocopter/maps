import json
import simplekml

def convert_json_to_kml(json_file, kml_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    kml = simplekml.Kml()

    for location in data['locations']:
        latitude = location['latitudeE7'] / 1e7
        longitude = location['longitudeE7'] / 1e7
        kml.newpoint(coords=[(longitude, latitude)])

    kml.save(kml_file)
