# Exercise 4 - collatz.py
# Mark Cotter, V1_01, 2019-02-17

# V1_01 - Program created 2019-02-17

# Asks a user to input any positive integer and
# tells the user whether the number is a prime.
# The program does nothing if the positive integer is not a prime.

# Set initial states for variables 'num' and 'i' to store the number
# and cycle through a range of numbers to look for a divisor of the number
num, i = 0, 0

# Request user to enter a positive integer and assign the value to 'num'
# Inputted value has to be an integer type value (not a float or string)
num = int(input("Please enter a positive integer: "))

# Check if inputted value for 'num' is a positive integer
# Loop until zero or a greater positive integer is entered
while num < 0:
# Print error if inputted value for 'num' is not a positive integer
    print("Input error -->",num ,"<-- is not a positive integer.")
# Request user to enter a new positive integer
    num = int(input("Please enter a positive integer: "))

# If the number is 0 or 1 DO nothing
# For the values of 2 or greater, check for divisors of 'num'
if num >= 2:
    for i in range(2, num):
        # Check if the number divides evenly into 'num'
        # If the modulus of dividing 'num' is zero
        if num % i == 0:
            # Stop the for loop if a divisor of 'num' is found
            break
    else:
        # If the break condition is not True the for loop could not find
        # a divisor of 'num' between 2 and 'num'
        # the 'num' value must be a prime number
        print("That is a prime.")

# Code reference sources:
# 1. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' asking user
#    to input a positive integer.
# 2. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January and February 2019
#    I adapted the lecture notes code about for loops and break
# 3. I adapted code from the python online tutorial webpage
#    https://docs.python.org/3/tutorial/controlflow.html 
#    to use a for loop and break to check if a number is a prime