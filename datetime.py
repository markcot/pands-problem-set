# Exercise 8 - Datetime.py
# Mark Cotter, V1_03, 2019-03-22

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

# Set variable 't' to current time
# Code adapted for printing the various year month day and time from webpage
# https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp

# Set 'weekday' to current day of the week
weekday = str(dt.datetime.now().strftime("%A"))
# Set 'month' to current month
month = str(dt.datetime.now().strftime("%B"))
# Set 'day' to current day of the month, set to int for reviewing suffix
day = int(dt.datetime.now().strftime("%d"))
# Set day suffix to 'th' by default
suffix = "th"
# Set 'year' to current year
year = str(dt.datetime.now().strftime("%Y"))
# Set 'hour' to current hour, set to int to remove leading zero
hour = int(dt.datetime.now().strftime("%I"))
# Set 'minute' to current minute
minute = str(dt.datetime.now().strftime("%M"))
# Set 'ampm' to current 12 clock morning or evening AM or PM
ampm = str(dt.datetime.now().strftime("%p"))

# Test for suffix change
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

# Set AM or PM to lower case
# Code adapted from Week 7 lecture
ampm = ampm.lower()

# Prints the result
print(f"{weekday}, {month} {day}{suffix} {year} at {hour}:{minute}{ampm}")

