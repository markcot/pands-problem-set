# Exercise 5 - secondstring.py
# Mark Cotter, V1_01, 2019-03-20

# V1_01 - Program created 2019-03-20

# Asks an user to input any a string and outputs every second word.

# Set initial states for variable 's' and array 'a' to store the string
# an array 'a' and a counter 'i'
s, a, i = "a", [], 0

# Request user to enter a sentence and assign the value to 's'
s = str(input("Please enter a sentence: "))
# Test print of sentence
#print(s)

# Code adapted from GMIT H Dip Data Analytics lecture video Week 7 March 2019
a = s.split()
# Test print of array
#print(a)

while i < len(a):
    print(a[i])
    i +=2
