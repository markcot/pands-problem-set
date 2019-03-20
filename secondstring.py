# Exercise 6 - secondstring.py
# Mark Cotter, V1_01, 2019-03-20

# V1_01 - Program created 2019-03-20

# Asks an user to input any a string and outputs every second word.

# Set initial states for string variable 's' store the string a counter 'i'
# and a result array 'r'
s, i, r = "", 0, []

# Request user to enter a sentence and assign the value to string variable 's'
s = str(input("Please enter a sentence: "))
# Test print of sentence
#print(s)

# Replace full stop and comma's with empty string element - Ignores colons
# Note if a number with decimal point is included in the sentence it will also
# be replaced. I.e. Test '1.0' will becom '10' after the . is replaced.
# Code adapted from website
# https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
s = s.replace(".", "")
s = s.replace(",", "")
# Test print of sentence
#print(s)

# Split the sentence into an array
# Code adapted from GMIT H Dip Data Analytics lecture video Week 7 - March 2019
# & https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
r = s.split()
# Test print of array
#print(r)

# Print each second word in the array 'r' (all the odd numbered words in the
# sentence), i starts at the first word r[0]
while i < len(r):
    # Add the word to the result array 'r'
    # Code adapted from Mark Cotter Exercise 4 - collatz.py
    print(r[i], end=' ')
    # jump to next second word in the array 'r'
    i += 2
