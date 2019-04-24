import csv, json
import string
from geojson import Feature, FeatureCollection, Point

features = []
with open('airport.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for latitude, longitude, name in reader:
        latitude.replace(" ", "")
        longitude.replace(" ", "")
        print (repr(latitude))
        print(len(latitude))
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'name': name,
                }
            )
        )

collection = FeatureCollection(features)
with open("data.geojson", "w") as f:
    f.write('%s' % collection)