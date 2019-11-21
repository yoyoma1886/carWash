import googlemaps
import pprint
import time
import json
import xlsxwriter
import tablib
import numpy
import pandas as pd
from pandas.io.json import json_normalize
import collections

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

stored_results = []

field_details = ['name', 'place_id', 'permanently_closed', 'adr_address', 'geometry/location', 'url',
                 'vicinity', 'formatted_address', 'address_component', 'formatted_phone_number', 'type']

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
                my_place_id = place['place_id']
                my_fields = field_details
                places_details = gmaps.place(
                    place_id=my_place_id, fields=my_fields)
                stored_results.append(places_details['result'])

            if len(places_result['results']) >= 20:
                time.sleep(2)

        except:
            pass

        try:
            places_result = gmaps.places_nearby(
                page_token=places_result['next_page_token'])

            for place in places_result['results']:
                my_place_id = place['place_id']
                my_fields = field_details
                places_details = gmaps.place(
                    place_id=my_place_id, fields=my_fields)
                stored_results.append(places_details['result'])

            if len(places_result['results']) >= 20:
                time.sleep(2)
        except:
            print("Nope")

        try:
            places_result = gmaps.places_nearby(
                page_token=places_result['next_page_token'])

            for place in places_result['results']:
                my_place_id = place['place_id']
                my_fields = field_details
                places_details = gmaps.place(
                    place_id=my_place_id, fields=my_fields)
                stored_results.append(places_details['result'])
        except:
            print("Nope")

df = json_normalize(stored_results, max_level=None)
print(df)


df.to_excel(r'C:\Users\rymur\Desktop\data.xlsx')


# df = pd.DataFrame.from_dict(json_normalize(stored_results), )
# print(df, sep='\n')

# print(json_normalize(stored_results))

# print(len(stored_results))

# def flatten(stored_results):
#     if isinstance(stored_results, collections.Iterable):
#         return [a for i in stored_results for a in flatten(i)]
#     else:
#         return [stored_results]

# flatten()


# pprint.pprint(stored_results)
# df = pd.DataFrame(stored_results), orient='columns')
# df
# print json_normalize(stored_results)
# print json_normalize (df)


# translate to Excel -----------------------------

# # define headers, the key of each result dictionary
# row_headers = stored_results[0].keys()

# # create new workbook and new worksheet
# workbook = xlsxwriter.Workbook(r'C:\Users\rymur\Desktop\data.xlsx')
# worksheet = workbook.add_worksheet()

# # populate the header row
# col = 0
# for header in row_headers:
#     worksheet.write(0, col, header)
#     col += 1

# row = 1
# col = 0
# # populate the other rows

# # get each result from the list
# for result in stored_results:

#     # get the values from each result
#     result_values = result.values()

#     # loop through each value in the values component
#     for value in result_values:
#         worksheet.write(row, col, value)
#         col += 1

#     # make sure to go to the next row @ reset the column
#     row += 1
#     col = 0

# # close the workbook
# workbook.close()
