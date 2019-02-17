# Exercise 3 - divisors.py
# Mark Cotter, V1_02 2019-02-17

# V1_02 - 2019-02-10
# Comments updated and if statement '&' replaced with 'and'
# Changed variable 'x' to 'i'

# V1_01 - Program created 2019-02-10

# Write a program that prints all numbers between 1,000 and 10,000
# that are divisible by 6 but not 12

# Assign variable 'a', 'b', 's' and 'e' for 'lower divisor' of 6,
# 'upper divisor' of 12 in the range 'starting' at 1,000 and 'ending' at 10,000
# Also use variable 'i' to search in the range of 's' to 'e'.
(a, b, s, e, i) = (6, 12, 1000, 10000, 1)

# Check print of values to be used
#print("The lower divisor is", a, "\n"
#    "The upper divisor is", b, "\n"
#    "The range is from", s, "to", e)

# Check values in range 's' to 'e' fulfil the
# True condition = "divisible by 'a' but not by 'b'"
# eg if the modulus when dividing 'i' by 'a' is = 0 and if the modulus of 
# dividing 'i' by 'b' is greater than zero.
# Use 'i' to search the range and print the number when the required condition
# is True
# The end of the range has to extended by +1 to ensure that the value of 'e'
# is also checked for the True condition.
for i in range(s, (e+1)):
    if (i % a == 0) and (i % b > 0):
        print(i)

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    January and February 2019
#    I adapted code from the lecture notes example of 'for' loops and remaining
#    fractions after divisions and to print numbers when modulus = 0 after division
#    I also adapted code for print statement over multiple line "\n"
# 2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
#    published by O'Rielly Media Inc. 2016
#    Reading first few chapters I adapted code for modulus if and elif for use
#    in this program.