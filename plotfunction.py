# Exercise 9 - plotfunction.py
# Mark Cotter, V1_01, 2019-03-23

# V1_01 - Program created 2019-03-23

# A program that displays a plot of the functions x, x^2 and 2^x in the
# range [0, 4].


# Set variables for range of the function
minrange, maxrange = 0, 4
# Set Initial variable for iterator i, and 3 arrays x, s (x square) and
# p (2 power of x)
i, x, s, p = 0, [], [], []

# Adds the numbers in the range into the array x
for i in range(minrange,(maxrange + 1)):
    x.append(i)

# Adds the square of numbers in x into the array s
for i in x:
    s.append(x[i] * x[i])

# Adds the 2 to power of numbers in x into the array p
for i in x:
    p.append(2 * x[i])

# Test prints of array contents
print(x)
print(s)
print(p)

