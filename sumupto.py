# Mark Cotter, V1_02, 2019-02-02

# Requests user to enter a positive integer 'i'
# The 'sum' of numbers between 1 and the 
# entered value of 'i' is outputed

# V1_02 update - OPTION 02 added if needed to keep user entered 'i' value
# Remove double comment ## below at OPTION 02 code loop, initial variable 
#   'x' and add ## to OPTION 01 loop code block to use OPTION 02

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
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
# 3. Web page:
#    https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html