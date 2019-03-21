# Exercise 7 - squareroot.py
# Mark Cotter, V1_01, 2019-03-21

# V1_01 - Program created 2019-03-21

# A program that that takes a positive ﬂoating point number as input
# and outputs an approximation of its square root

# Calculates the square root based on the Babylonian square-root algorithm
# found on webpage
# https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

# Set initial states for float variable 'num' and the square root 'root'
num, root = 1.0, 1.0

# Request user to enter a sentence and assign the value to variable 'num'
num = float(input("Please enter a positive number: "))

# Check if inputted value for 'num' is a positive
# Loop until a positive non-zero number is entered
# Code adapted from Mark Cotter Exercise 1 - sumupto.py
while num < 0:
# Print error if inputted value for 'i' is not a positive number
    print("Input error -->",num,"<-- is not a positive number")
# Request user to enter a new positive number
    num = float(input("Please enter a positive number: "))

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
while abs(root - (num / root)) > 0.01:
    root = (root + (num / root)) / 2

# Round root to one decimal place
# Adapted round function code from website
# https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830
root = round(root,1)

# Prints the result
print(f"The square root of {num} is approx. {root}.")
