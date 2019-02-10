# Mark Cotter, V1_01, 2019-02-10

# V1_01 - Program created 2019-02-10

# Asks a user to input any positive integar and
# Outputs the sucessive values of the following calculation
# At each step calculate the next value by taking the current value and
# if it even, divide it by 2 
# but if it odd, multiply it by three and add one
# End the program when the current value it one.

# Set intial states for variable 'i' for 'Inputed value apply calculations to
# Also used at the end of the program to cycle through list 'l'
i = 0
# Create an empty list 'l'
l = []

# Request user to enter a positive integer and assign the value to 'i'
# Inputed value has to be an integer type value (not a float or string)
i = int(input("Please enter a positive integer: "))

# Check if inputed value for 'i' is a positive integer
# Loop until a positive integar is entered
while i < 1:
# Print error if inputed value for 'i' is not a positive integer
    print("Input error -->",i,"<-- is not a positive integer")
# Request user to enter a new positive integer
    i = int(input("Please enter a positive integer: "))

# Add the first value of i to end of list 'l'
l.append(i)

# Loop until the last value in list 'l' is equal to 1
while (l[-1] != 1):
    # Check if last value in list 'l' is even
    if (l[-1] % 2) == 0:
        # Divide the last number in list 'l' by 2 if it is even
        # and make i an integar and not a float
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

# Reuse 'i' reset its state = 0
i = 0
# Print the list 'l' on a single line without [] bracket to commas,
# For each item over the length of the list 'l' print that in a line
# with just a space between each item from the list
for i in range(0,len(l)):
    # Print the value for item in list 'l' which corresponds with the 
    # position of 'i' in the list.
    print(l[i], end=' ')
    # Add 1 to 'i' to look at the next item in the list 'l'
    i += 1

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    Janurary 2019
#    I adapted the lecture notes while loop and discussion about lists
#    and the appending items to lists.
# 2. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' and Exercise 3
#    divisors.py asking user to input a positive integar check if it even or odd
#    by checking the modulas after dividing by 2 is = 0
# 3. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted code for not equal to != if and
#    elif for use in this program.
# 4. I adpated code the the folowing python tutorial webpage about lists
#    and appending list. I adpated code in a 'while' loop to create a 'for' loop
#    to print all the values in the list 'l' with a space separator only
#    print( , end=' ')
#    https://docs.python.org/3/tutorial/introduction.html#lists
#    https://docs.python.org/3/tutorial/datastructures.html













