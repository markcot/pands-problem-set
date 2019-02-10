# Mark Cotter, V1_04, 2019-02-10

# Requests user to enter a positive integer 'i'
# The 'sum' of numbers between 1 and the 
# entered value of 'i' is outputed

# V1_04 update 2019-02-10
# Comments updated

# V1_03 update 2019-02-09
# Reference and comments updated

# V1_02 update 2019-02-02
# OPTION 02 added if needed to keep user entered 'i' value
# Remove double comment ## below at OPTION 02 code loop, initial variable 
#   'x' and add ## to OPTION 01 loop code block to use OPTION 02

# V1_01 - Program created 2019-02-01

# Set intial states for variables 'i', 'x' and 'sum'
i = 1
sum = 0
# Additional OPTION 02 variable
##x = 0

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

# Calculates the 'sum' of numbers from 1 to 'i' OPTION 01
# This option only requires TWO variable 'i' and 'sum'
# Note that the final state value of 'i' is reduced to 0
while i > 0:
    sum += i
    i -= 1

# Calculates the 'sum' of numbers from 1 to 'i' OPTION 02
# This option requires THREE variable 'i', 'x' and 'sum'
# Note that the final state value of 'i' remains as the user entered value
##for x in range(1,(i + 1)):
##    sum += x

# Check prints of the final states of 'i' and 'x'
#print("Final state of variable 'i' is",i)
#print("Final state of variable 'x' is",x)

# Prints the 'sum' of numbers from 1 to user entered value for 'i'
print(sum)

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    Janurary 2019
#    I adapted the lecture notes while loop to count down to 0 from i so
#    that I could leave out a counter variable
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted shorted version code for adding
#    the sum to it's self and operators '+=' and '-='
# 3. I adapted code on the following web page to request user to input a value
#    and make that value an integer.
#    https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html