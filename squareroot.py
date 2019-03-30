# Exercise 7 - squareroot.py
# Mark Cotter, V1_02, 2019-03-30

# V1_02 - 2019-03-30
# Removed the loop for continuosly requesting new values for 'num'.
# Added input type checking with try function
# Comments updated.

# V1_01 - Program created 2019-03-21

# A program that that takes a positive ﬂoating point number as input
# and outputs an approximation of its square root

# Calculates the square root based on the Babylonian square-root algorithm
# found on webpage
# https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

# Set initial states for float variable 'num' and the square root 'root'
num, root = 1.0, 1.0

# Request user to enter a sentence and assign the value to variable 'num'
num = input("Please enter a positive number: ")

# Try to check if inputted value for 'num' is a positive number
# Code adapted from Week 10 lecture & Exercise 5 - primes.py
try:
    # Try to convert 'num' to an float type
    num = float(num)
    # If 'num' is an positive number
    if num >= 0.0:
        # Set first approximation of 'root' to half of 'num'
        root = num / 2
        # Test print
        #print(num)
        #print(root)

        # Calculate the approximate square root of 'num' using Babylonian square-root
        # algorithm. Code adapted from algorithm on webpage
        # https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

        # Loop until the difference between 'root' and
        # 'num' divided by 'root' gives a value less than 0.01
        # Code adapted from Week 8 lecture
        while abs(root - (num / root)) > 0.01:
            root = (root + (num / root)) / 2

        # Round root to one decimal place
        # Adapted round function code from website
        # https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830
        root = round(root,1)

        # Prints the result
        # Formated print code adpted from Week 7 lecture.
        print(f"The square root of {num} is approx. {root}.")
    
    # Otherwise prints a VALUE error message if 'num' is not a positive number
    else:
        print(f"Input Error: --> {num} <-- is not a positive number.")

# Prints a TYPE exception error if 'num' not a number type variable
except:
    print(f"Input Error: --> {num} <-- is not a number.")

# Code reference sources:
# 1. Code adapted for Babylonian square-root algorithm found on webpage
#    https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html
#
# 2. Code adapted from Exercise 5 - primes.py and Week 10 lectures for checking
#    for inputted values with try and except functions
#
# 3. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    I adapted code from the Week 8 lecture for looping a square root
#
# 4. Code for rounding number to one decimal place adapted from website
#    https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830
#
# 5. Formated print statement code adapted from Week 7 lecture.