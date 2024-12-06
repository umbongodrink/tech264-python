# Zen of Python
# import this

import random



print(random.randrange(1, 100))

import math, os

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
# gives us remainder of the 2 values# 5 can't go into 1, so the remainder is 1
print(f"Remainder from 1/5: {math.remainder(1, 5)}")

# returns our current working directoryworking_directory = os.getcwd()print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")


import datetime

# gives us today's date
print(f"Today's date: {datetime.date.today()}")


