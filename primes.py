# Exercise 5 - primes.py
# Mark Cotter, V1_03, 2019-03-30

# V1_03 - 2019-03-30
# Comments updated.

# V1_02 - 2019-03-30
# Removed the loop for continuosly requesting new values for 'i'.
# Added input type checking with try function
# Added print for when the number is not a prime
# Comments updated.

# V1_01 - Program created 2019-02-17

# Asks a user to input any positive integer and
# tells the user whether or not the number is a prime.
#
# Note: that in the event of the user input NOT being a
# positive interger, the program prints an error message and
# does not compute anything.

# Set initial states for variables 'num' and 'i' to store the number
# and cycle through a range of numbers to look for a divisor of the number
num, i = 0, 0

# Request user to enter a positive integer and assign the value to 'num'
# Inputted value has to be an integer type value (not a float or string)
num = input("Please enter a positive integer: ")

# Try to check if inputted value for 'num' is a positive integer
# Code adapted from Week 10 lecture & Exercise 4 - collatz.py
try:
    # Try to convert 'num' to an integer type
    num = int(num)
    # If 'i' is an positive integer
    if num >= 0:
        # If the number is 0
        if num == 0:
            # Prints that the number is not a prime
            print("That is not a prime.")
        # If the number is 1
        elif num == 1:
            # Prints that the number is not a prime
            print("That is not a prime.")
        # For the values of 2 or greater, check for divisors of 'num'
        elif num >= 2:
            # Code adapted from https://docs.python.org/3/tutorial/controlflow.html 
            for i in range(2, num):
                # Check if the number divides evenly into 'num'
                # If the modulus of dividing 'num' is zero
                if num % i == 0:
                    # Divisor found, Print that the number is not a prime
                    print("That is not a prime.")
                    # Stop the for loop if a divisor of 'num' is found
                    break
            else:
                # If the break condition is not True the for loop could not find
                # a divisor of 'num' between 2 and 'num'
                # the 'num' value must be a prime number
                print("That is a prime.")
    # Otherwise prints a VALUE error message if 'num' is not a positive integer
    else:
        print("Input Error: -->", num, "<-- is not a positive integer.")

# Prints a TYPE exception error if 'num' not an integer
except:
    print("Input Error: -->", num, "<-- is not an integer type.")

# Code reference sources:
# 1. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' asking user
#    to input a positive integer.
#
# 2. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January and February 2019
#    I adapted the lecture notes code about for loops and break
#
# 3. I adapted code from the python online tutorial webpage
#    https://docs.python.org/3/tutorial/controlflow.html 
#    to use a for loop and break to check if a number is a prime
#
# 4. Code adapted from Exercise 4 - collatz.py and Week 10 lectures for checking
#    for inputted values with try and except functions