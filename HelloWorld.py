import math
from os import rename
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


r = requests.get('https://coreyms.com')
print(r.status_code)

# 51 minutes, trying to install git - email
