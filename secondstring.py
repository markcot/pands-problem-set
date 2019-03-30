# Exercise 6 - secondstring.py
# Mark Cotter, V1_02, 2019-03-30

# V1_02 - 2019-03-30
# Comments updated.

# V1_01 - Program created 2019-03-20

# Asks an user to input any a string and outputs every second word.

# Set initial states for string variable 's' store the string a counter 'i'
# and a result list 'r'
s, i, r = "", 0, []

# Request user to enter a sentence and assign the value to string variable 's'
s = str(input("Please enter a sentence: "))
# Test print of sentence
#print(s)

# Replace full stop and comma's with empty string element - Ignores colons
# Note if a number with decimal point is included in the sentence it will also
# be replaced. I.e. Test '1.0' will become '10' after the . is replaced.
# Code adapted from website
# https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
s = s.replace(".", "")
s = s.replace(",", "")
# Test print of sentence
#print(s)

# Split the sentence into an list
# Code adapted from GMIT H Dip Data Analytics lecture video Week 7 - March 2019
# & https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
r = s.split()
# Test print of list
#print(r)

# Print each second word in the list 'r' (all the odd numbered words in the
# sentence), i starts at the first word r[0]
while i < len(r):
    # Add the word to the result list 'r'
    # Code adapted from Mark Cotter Exercise 4 - collatz.py
    print(r[i], end=' ')
    # jump to next second word in the list 'r'
    i += 2

# Code reference sources:
# 1. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' asking user
#    to input a positive integer or string. 
#
# 2. Code for replacing commas and full-stops adapted from website 
#    https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
#
# 3. Code for spliting the sentence into an list adapted from GMIT H Dip Data
#    Analytics lecture video Week 7 - March 2019 & website
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 4. Mark Cotter February 2019 code for Exercise 4 - collatz.py' for print from
#    an list onto one line.