# Exercise 9 - second.py
# Mark Cotter, V1_05, 2019-03-30

# V1_05 - 2019-03-30
# Comments updated
# 'lcount' variable added if needed for varying division of lines (second/third/etc.)

# V1_04 - 2019-03-23
# File input changed to use sys.args to callup the reading of the file
# Error check if text filename is missing from the command line input

# V1_03 - 2019-03-23
# Minor amendment made to if loop and i variable
# Filename module added and input file now taken from the command line

# V1_02 - 2019-03-23
# Code added to print every second line of the text

# V1_01 - Program created 2019-03-22

# A program that reads in a text ﬁle and outputs every second line. The program
# takes a single additional filename from an argument on the command line.
#
# Note that a single additional text filename has to be specified after the program
# name. e.g. >>python second.py moby-dick.txt
# The program prints an error if no additional filename is provided
# The program prints an error if two or more additional filenames are provided 

# variable counter i & Line counter 'lcount'
# 'lcount' can be set to 2, 3, 4, 5 etc. for every second, third, fourth or
# fifth line respectively as required
i, lcount = 0, 2

# variable f is for the file name loaded
# variable line is for reading each line in the file f

# Opens the python sys module
# Code verbatim from Week 9 lecture of command line arguments in python
import sys

# Test to check if number of arguments supplied is = 2
# Code adapted from Week 9 lecture of command line arguments in python
if len(sys.argv) != 2:
    # print error message and the program does nothing
    print("Input Error: A single filename for input should be included.")
else:
    # Otherwise do the following
    # Open the file at the second argument called on the command line
    # i.e. open the text file as read only as variable 'f'
    # The formated code with {} refers to the second argument of the python
    # list on the command line do the open command opens the first file after
    # >>python second.py ...
    # on the command line.
    # Code adapted from Week 9 lecture
    with open(f'{sys.argv[1]}', 'r') as f:
        # For each line in file f read the line
        for line in f:
            # Remove additional line breaks
            # Code adapted from Week 7 lecture
            line = line.rstrip("\n")
            # check for start of every 'lcount' line, starting with first line as 0
            if i % lcount == 0:
                # print the every 'lcount' line starting with the first line
                print(line)
            # Increment i
            i += 1
    # closes the file f
    # Code verbatim from Week 9 lecture
    f.close()
# End of program

# Code reference sources:
# 1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#    Some code verbatim and other code adapted from the Week 9 lecture for importing
#    the sys module and using the sys.argv function and printing Error message and
#    closing files.
#
# 2. Code adapted for striping additional line break adapted from Week 7 lecture.