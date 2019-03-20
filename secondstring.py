# Exercise 5 - secondstring.py
# Mark Cotter, V1_01, 2019-03-20

# V1_01 - Program created 2019-03-20

# Asks an user to input any a string and outputs every second word.

# Set initial states for variable 's' and array 'a' to store the string
# an array 'a' and a counter 'i' and result array 'r'
s, a, i, r = "", [], 0, []

# Request user to enter a sentence and assign the value to string variable 's'
s = str(input("Please enter a sentence: "))
# Test print of sentence
#print(s)

# Replace full stop and comma's with empty string element - Ignores colons
# Code adapted from website
# https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
s = s.replace(".", "")
s = s.replace(",", "")
# Test print of sentence
#print(s)

# Split the sentence into an array
# Code adapted from GMIT H Dip Data Analytics lecture video Week 7 - March 2019
# & https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
a = s.split()
# Test print of array
#print(a)

# for each second word in the array 'a' add the word into array 'r'
# i starts at the first word a[0]
while i < len(a):
    # Add the word to the result array 'r'
    r.append(a[i])
    # jump to next second word in the array
    i += 2

# Reuse 'i' and reset its state = 0
i = 0
# Print the array 'r' on a single line without [] brackets or commas,
# For each item over the length of the array 'r' print that value in a line
# with just a space between each item from the array
# Code adapted from Mark Cotter Exercise 4 - collatz.py
for i in range(0,len(r)):
    # Print the value for item in array 'r' which corresponds with the 
    # position of 'i' in the array.
    print(r[i], end=' ')
    # Add 1 to 'i' to look at the next item in the array 'r'
    i += 1