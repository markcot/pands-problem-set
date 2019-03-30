# Exercise 1 - sumupto.py
# Mark Cotter, V1_06, 2019-03-30

# Requests user to enter a positive integer 'i'
# The 'sum' of numbers between 1 and the 
# entered value of 'i' is outputted
#
# Note: that in the event of the user input NOT being a
# non-zero positive interger, the program prints an error message and
# does not compute anything.

# V1_06 update 2019-03-30
# Input exception check added. Removed OPTION 02 and the loop for
# continuosly requesting new values for 'i'.

# V1_05 update 2019-02-17
# Comments updated

# V1_04 update 2019-02-10
# Comments updated

# V1_03 update 2019-02-09
# Reference and comments updated

# V1_02 update 2019-02-02
# OPTION 02 added if needed to keep user entered 'i' value
# Remove double comment ## below at OPTION 02 code loop, initial variable 
#   'x' and add ## to OPTION 01 loop code block to use OPTION 02

# V1_01 - Program created 2019-02-01

# Start of program
# Set initial states for variables 'i' and 'sum'
i, sum = 1, 0

# Request user to enter a positive integer and assign the value to 'i'
# Inputted value has to be an integer type value (not a float or string)
# Code adapted from https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
i = (input("Please enter a positive integer: "))

# Try to check if inputted value for 'i' is a positive integer
# Code adapted from Week 10 lecture
try:
    # Try to convert 'i' to an integer type
    i = int(i)
    # If 'i' is an non-zero positive integer
    if i > 0:
        # Calculates the 'sum' of numbers from 1 to 'i'
        # Note that the final state value of 'i' is reduced to 0
        while i > 0:
            # Increment 'sum' with value of 'i'
            # Code adapted from book 'A Whirlwind Tour of Python'
            sum += i
            # Decrement 'i'
            # Code adapted from book 'A Whirlwind Tour of Python'
            i -= 1

        # Check prints of the final state of 'i', Note 'i' reduces to zero
        #print("Final state of variable 'i' is",i)

        # Prints the 'sum' of numbers from 1 to user entered value for 'i'
        print(sum)
    # Otherwise prints a VALUE error message if 'i' is not an integer > 0
    else:
        print("Input Error: -->", i, "<-- is not a non-zero positive integer.")

# Prints a TYPE exception error if 'i' not an integer
except:
    print("Input Error: -->", i, "<-- is not an integer type.")



# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January 2019
#    I adapted the lecture notes while loop to count down to 0 from i so
#    that I could leave out a counter variable
#
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted shorted version code for adding
#    the sum to it's self and operators '+=' and '-='
#
# 3. I adapted code on the following web page to request user to input a value
#    and make that value an integer.
#    https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
#
# 4. I adapted code from Week 10 lecture in relation try and except for exceptions.