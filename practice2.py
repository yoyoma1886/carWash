import googlemaps
import pprint
import time
import json
import xlsxwriter
import tablib
import numpy

# Define API Key
API_KEY = "AIzaSyDy1kLx1ELKzyrC2QyIOeUtbNCRK1NZQWc"

# define client
gmaps = googlemaps.Client(key=API_KEY)

# Location search (nearby) ----------------------------------------

# NJ coordinates: N: 41.362939 / S: 38.927599, W: -75.558906, E: -73.975784
# 10 N/S iterations, 5 W/E

xMax = 41.362939
yMax = -75.558906

xMin = 38.927599
yMin = -73.975784

xTurns = -numpy.divide(xMax-xMin, 2)
yTurns = -numpy.divide(yMax-yMin, 2)

store = []

my_place_id = place['place_id']
my_fields = ['name', 'place_id']

for x in numpy.arange(xMax, xMin, xTurns):
    for y in numpy.arange(yMax, yMin, yTurns):

        params = {
            'location': (x, y),
            'radius': 5000,
            'type': "car_wash"
        }
        try:
            places_result = gmaps.places_nearby(**params)

            for place in places_result['results']:
                places_details = gmaps.place(
                    place_id=my_place_id, fields=my_fields)
                stored_results.append(places_details['result'])

            store.append(places_result['results'])

            if len(places_result['results']) >= 20:
                time.sleep(2)

        except:
            pass

        try:
            places_result = gmaps.places_nearby(
                page_token=places_result['next_page_token'])
            pprint.pprint(len(places_result['results']))
            store.append(places_result['results'])

            if len(places_result['results']) >= 20:
                time.sleep(2)
        except:
            print("Nope")

        try:
            places_result = gmaps.places_nearby(
                page_token=places_result['next_page_token'])
            pprint.pprint(len(places_result['results']))
            store.append(places_result['results'])
        except:
            print("Nope")

# print(*store)

# pprint.pprint(store)

# #         # define the place ID, needed to get details, as string
# my_place_id = place['place_id']

# # define fields to return, formatted as list
# my_fields = ['name']

# # make request for details
# places_details = gmaps.place(
#     place_id=my_place_id, fields=my_fields)

# # print results of details, as dictionary
# pprint.pprint(places_details['result'])
