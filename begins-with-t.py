# Exercise 2 - begins-with-t.py
# Mark Cotter, V1_05, 2019-03-30

# Check if today is a day that begins with the letter 'T'
# (i.e. 'Tuesday' or 'Thursday')
# Outputs 'Yes' if today begins with a 'T'
# Outputs 'No' if today does not begin with a 'T'

# V1_05 update 2019-03-30
# Comments updated

# V1_04 update 2019-02-17
# Comments updated

# V1_03 update 2019-02-10
# Comments updated

# V1_02 update 2019-02-09
# Reference and comments updated

# V1_01 - Program created 2019-02-02

# Set initial state of string variable 'today' for the day of the week
today = "Monday"
# Interim check print of initial state of variable 'today'
#print("First variable 'today' is set to",today)

# Import current date
import datetime

# Assign the current day of the week string format to variable 'today'
# Code adapted from
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
today = str(datetime.datetime.today().strftime('%A'))
# Interim check what day is today
#print("Today is", today)

# Check if first letter in sting variable 'today' is 'T'
# Code adapted from 'A Whirlwind Tour of Python' &
# https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list
if (today[0]) == str("T"):
# Print 'Yes' if today begins with a 'T'
    print("Yes - today begins with a T.")
else:
# Otherwise print 'No'
    print("No - today does not begin with a T.")

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January 2019
#    I adapted code from the lecture notes example Python-Tuesday for checking
#    what todays day of the week is.
#
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted code for if and elif for use in this
#    program.
#
# 3. I adapted code from the following webpage to return a string for the
#    current day of the week
#    https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
#
# 4. I adapted code from the following webpage to return the first character
#    of a text string. This was covered also in a later GMIT lecture
#    https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list