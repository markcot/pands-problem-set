# Exercise 4 - collatz.py
# Mark Cotter, V1_04, 2019-03-30

# V1_04 - 2019-03-30
# Minor Comment updates. Removed the loop for
# continuosly requesting new values for 'i'.
# Added input type checking with try function

# V1_03 - 2019-02-17
# Minor Comment updates

# V1_02 - 2019-02-10
# Minor Comment updates

# V1_01 - Program created 2019-02-10

# Asks a user to input any positive integer and
# Outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and
# if it even, divide it by 2 
# but if it odd, multiply it by three and add one
# End the program when the current value is one.
#
# Note: that in the event of the user input NOT being a
# non-zero positive interger, the program prints an error message and
# does not compute anything.

# Set initial states for variable 'i' for 'Inputted value' to apply calculations
# Also used at the end of the program to cycle through a list 'l'
i = 1
# Create an empty list 'l'
l = []

# Request user to enter a positive integer and assign the value to 'i'
# Inputted value has to be an integer type value (not a float or string)
i = input("Please enter a positive integer: ")

# Try to check if inputted value for 'i' is a positive integer
# Code adapted from Week 10 lecture & Exercise 1 - sumupto.py
try:
    # Try to convert 'i' to an integer type
    i = int(i)
    # If 'i' is an non-zero positive integer
    if i > 0:
        # Add the first value of i to end of list 'l'
        l.append(i)

        # Loop until the last value in list 'l' is equal to 1
        while (l[-1] != 1):
            # Check if last value in list 'l' is even
            # Code adapted from Exercise 3 divisors.py
            if (l[-1] % 2) == 0:
                # Divide the last number in list 'l' by 2 if it is even
                # and make i an integer and not a float
                i = int(l[-1] / 2)
                # Add the calculated value of i to end of list 'l'
                l.append(i)
            else:
                # If not even the last number in list 'l' is odd
                # So multiply it by three and add one
                i = (l[-1] * 3) + 1
                # Add the calculated value of i to end of list 'l'
                l.append(i)

        # Check print for list 'l'
        #print(l)

        # Reuse 'i' and reset its state = 0
        i = 0
        # Print the list 'l' on a single line without [] brackets or commas,
        # For each item over the length of the list 'l' print that value in a line
        # with just a space between each item from the list
        for i in range(0,len(l)):
            # Print the value for item in list 'l' which corresponds with the 
            # position of 'i' in the list.
            # Code adapted from
            # https://docs.python.org/3/tutorial/introduction.html#lists
            # https://docs.python.org/3/tutorial/datastructures.html
            print(l[i], end=' ')
            # Add 1 to 'i' to look at the next item in the list 'l'
            i += 1
    # Otherwise prints a VALUE error message if 'i' is not an integer > 0
    else:
        print("Input Error: -->", i, "<-- is not a non-zero positive integer.")

# Prints a TYPE exception error if 'i' not an integer
except:
    print("Input Error: -->", i, "<-- is not an integer type.")


# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January and February 2019
#    I adapted the lecture notes while loop and discussion about lists
#    and appending items to lists.
#
# 2. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' and Exercise 3
#    divisors.py asking user to input a positive integer check if it even or odd
#    by checking the modulus after dividing by 2 is = 0
#
# 3. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted code for not equal to != if and
#    elif for use in this program.
#
# 4. I adapted code from the following python tutorial webpage about lists
#    and appending list. I adapted code in a 'while' loop to create a 'for' loop
#    to print all the values in the list 'l' with a space separator only
#    print( , end=' ')
#    https://docs.python.org/3/tutorial/introduction.html#lists
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 5. Code adapted from Exercise 1 - sumupto.py and Week 10 lectures for checking
#    for inputted values with try and except functions













