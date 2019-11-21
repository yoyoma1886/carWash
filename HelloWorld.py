import googlemaps
import pprint
import time
import json
import xlsxwriter
import tablib
import numpy
# from pandas.io.json import json_normalize
import pandas as pd
import collections

sales = [('Jones', 150, 200, 50),
         ('Alpha', 200, 210, 90)]

labels = ['account', 'jan', 'feb', 'mar']

df = pd.DataFrame(sales)
print(df)
