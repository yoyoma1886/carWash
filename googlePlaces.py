# pip install google maps
# pip install prettyprint

# TO FIX: next page token, address component handling (tuple), error when 0 responses,
# TO ADD: adding results to existing or new tab (not overwriting), API key method, iterative lat/long

import googlemaps
import pprint
import time
import json
import xlsxwriter
import tablib

# Define API Key
API_KEY = "AIzaSyDy1kLx1ELKzyrC2QyIOeUtbNCRK1NZQWc"

# define client
gmaps = googlemaps.Client(key=API_KEY)

# Location search (nearby) ----------------------------------------

# NJ coordinates: N: 41.362939 / S: 38.927599, W: -75.558906, E: -73.975784

params = {
    'location': (40.906620, -74.611021),
    'radius': 5000,
    'type': "car_wash"
}

places_result = gmaps.places_nearby(**params)

time.sleep(2)

# pass next page token for add'l 20 results
# params['page_token'] = places_result['next_page_token']

# run gmaps again with next token
# place_result = gmaps.places_nearby(**params)

stored_results = []

# loop through each place to get details -----------------------------------

for place in places_result['results']:

    # define the place ID, needed to get details, as string
    my_place_id = place['place_id']

    # define fields to return, formatted as list
    my_fields = ['name', 'place_id']

#   POSSIBLE FIELDS = ['name', 'place_id', 'permanently_closed', 'formatted_address', 'address_component',
    #                'formatted_phone_number', 'geometry', 'type']

    # make request for details
    places_details = gmaps.place(place_id=my_place_id, fields=my_fields)

    # print results of details, as dictionary
    # pprint.pprint(places_details['result'])

    # store the results in a list object
    stored_results.append(places_details['result'])

    pprint.pprint(stored_results)

# translate to Excel -----------------------------

# define headers, the key of each result dictionary
row_headers = stored_results[0].keys()

# create new workbook and new worksheet
workbook = xlsxwriter.Workbook(r'C:\Users\rymur\Desktop\data.xlsx')
worksheet = workbook.add_worksheet()

# populate the header row
col = 0
for header in row_headers:
    worksheet.write(0, col, header)
    col += 1

row = 1
col = 0
# populate the other rows

# get each result from the list
for result in stored_results:

    # get the values from each result
    result_values = result.values()

    # loop through each value in the values component
    for value in result_values:
        worksheet.write(row, col, value)
        col += 1

    # make sure to go to the next row @ reset the column
    row += 1
    col = 0

# close the workbook
workbook.close()
