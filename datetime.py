# Exercise 8 - Datetime.py
# Mark Cotter, V1_04, 2019-03-23

# V1_04 - 2019-02-23
# Variables initial values added
# Minor comments added

# V1_03 - 2019-02-22
# Amendment made to day of month suffix.
# Comments added

# V1_02 - 2019-02-22
# Added functions to change day of month suffix to display, display PM/AM as
# lower case and remove unnecessary 0 from the text.

# V1_01 - Program created 2019-03-21

# A program that that outputs today's date and time in the format
# "Monday, January 10th 2019 at 1:15pm".

# Import the datetime module abbreviated to 'dt'
# Note the name of this program has to have a capital letter 'Datetime.py'
# as the function 'datetime' will not work if the program name is the same i.e.
# 'datetime.py'
import datetime as dt

# Initial variable values for 'year' 'month' 'day' 'suffix' 'weekday' 'hour'
# 'minute' and 'ampm'
year = 2019
month = "January"
day = 1
suffix = "st"
weekday = "Monday"
hour = 0
minute = "00"
ampm = "am"

# Set variable 't' to current time
# Code adapted for printing the various year month day and time from webpage
# https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
# and Exercise 2 - begins-with-t.py

# Set 'year' to current year, int because will always be 4 digits
year = int(dt.datetime.now().strftime("%Y"))
# Set 'month' to current month, str because is a word
month = str(dt.datetime.now().strftime("%B"))
# Set 'day' to current day of the month, int for reviewing suffix & removing lead 0
day = int(dt.datetime.now().strftime("%d"))
# Set 'weekday' to current day of the week, str because is a word
weekday = str(dt.datetime.now().strftime("%A"))
# Set 'hour' to current hour, int to remove leading zero
hour = int(dt.datetime.now().strftime("%I"))
# Set 'minute' to current minute, str because always want 2 digits
minute = str(dt.datetime.now().strftime("%M"))
# Set 'ampm' to current 12 clock morning or evening i.e. 'AM' or 'PM'
ampm = str(dt.datetime.now().strftime("%p"))

# Set AM or PM to lower case
# Code adapted from Week 7 lecture
ampm = ampm.lower()

# Temporary variable setting for suffix change test
#day = 31

# Add suffix to the day of the month
if day == 1:
    # Add abbreviated suffix for first
    suffix = "st"
elif day == 2:
    # Add abbreviated suffix for second
    suffix = "nd"
elif day == 3:
    # Add abbreviated suffix for third
    suffix = "rd"
elif day == 21:
    # Add abbreviated suffix for twenty first
    suffix = "st"
elif day == 22:
    # Add abbreviated suffix for twenty second
    suffix = "nd"
elif day == 23:
    # Add abbreviated suffix for twenty third
    suffix = "rd"
elif day == 31:
    # Add abbreviated suffix for thirty first
    suffix = "st"
else:
    suffix = "th"

# Prints the result
print(f"{weekday}, {month} {day}{suffix} {year} at {hour}:{minute}{ampm}")

