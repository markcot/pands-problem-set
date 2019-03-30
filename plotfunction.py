# Exercise 10 - plotfunction.py
# Mark Cotter, V1_03, 2019-03-30

# V1_03 - 2019-03-30
# Comments updated

# V1_02 - 2019-03-23
# Numpy array section added
# matplotlib.pyplot.plot function added to plot a line graph
# of the 3 function x, x^2 and 2^x versus the value of x.

# V1_01 - Program created 2019-03-23

# A program that displays a plot of the functions x, x^2 and 2^x in the
# range [0, 4].

# import matplotlib pyplot module abbreviated to pl
# Code verbatim from Week 9 lecture
import matplotlib.pyplot as pl
# import numpy module
import numpy

# Set variables for range of the function
minrange, maxrange = 0, 4

# Adds the numbers in the min to max range into the array x
# Code adapted from webpage
# https://physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html
x = numpy.arange(minrange, (maxrange +1), 1)

# Test prints of array contents
#print(x)
#print(x**2)
#print(2**x)

# plot the functions x versus x as a green line, x versus x squared as a blue
# line and x versus 2 to the power of x as a red line
# Code adapted from https://matplotlib.org/users/pyplot_tutorial.html
pl.plot(x, x, 'g-', x, x**2, 'b-', x, 2**x, 'r-')
# Add label to x axis
# Code adapted from https://matplotlib.org/users/pyplot_tutorial.html
pl.xlabel('Values of x')
# Edit x axis interval. Code adapted from
# https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
pl.xticks(numpy.arange(minrange, (maxrange + 1), 1.0))
# Add label to y axis
# Code adapted from
# https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
pl.ylabel('Green line = x vs. x\nBlue line = x vs. x^2\nRed line = x vs. 2^x')
# Show the plot of x, x^2 and 2^x
# Code verbatim from Week 9 lecture
pl.show()
# End of program

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    Some code verbatim and other code adapted from the Week 9 lecture for plotting
#    using matplotlib and numpy modules
#
# 2. Code adapted for setting min to max numpy array values from website
#    https://physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html
#
# 3. Code adapted for ploting using matplotlib from website
#    https://matplotlib.org/users/pyplot_tutorial.html
#
# 4. Code adapted for add label to x and y axes from website
#    https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib