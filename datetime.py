# Exercise 8 - Datetime.py
# Mark Cotter, V1_01, 2019-03-21

# V1_01 - Program created 2019-03-21

# A program that that outputs today's date and time in the format
# "Monday, January 10th 2019 at 1:15pm".

# Import the datetime module abbreviated to 'dt'
import datetime as dt

# Set variable 't' to current time
# Code adapted for printing the various year month day and time from webpage
# https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
# 2 problems 
# 1) Getting the st, nd, rd or th to display after the day for 1st, 2nd, 3rd, 4th, etc.
# 2) To get the PM after the minutes to display as lower case.
# I may need a few if loops prior to the printing the information
print(dt.datetime.now().strftime("%A, %B %d %Y at %I:%M%p"))
