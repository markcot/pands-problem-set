# Mark Cotter, V1_02, 2019-02-09

# Check if today is a day that begins with the letter 'T'
# (i.e. 'Tuesday' or 'Thursday')
# Outputs 'Yes' if today begins with a 'T'
# Outputs 'No' if today does not begin with a 'T'

# Set intial state of string variable 'today' for the day of the week
today = "Monday"
# Interim check print of intial state of variable 'today'
#print("First variable 'today' is set to",today)

# Import current date
import datetime

# Assign the current day of the week string format to variable 'today'
today = str(datetime.datetime.today().strftime('%A') )
# Interim check what day is today
#print("Today is",today)

# Check if first letter in sting variable 'today' is 'T'
if (today[0]) == str("T"):
# Print 'Yes' if today begins with a 'T'
    print("Yes - today begins with a T.")
else:
# Otherwise print 'No'
    print("No - today does not begin with a T.")

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    Janurary 2019
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
# 3. I adapted code from the following webpage to return a string for the
#    current day of the week
#    https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
# 4. I adapted code from the following webpage to return the first character
#    of a text string. This was covered also in a later GMIT lecture
#    https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list