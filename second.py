# Exercise 9 - second.py
# Mark Cotter, V1_04, 2019-03-23

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
# takes the filename from an argument on the command line.
# The filename has to be specified after the program name.
# I.e. 'python second.py moby-dick.txt'
# Otherwise the program will output an Error message

# variable counter i
i = 0
# variable f is for the file name loaded
# variable line is for reading each line in the file f

# Input file for reading
# Code adapted from websites
# https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
# https://docs.python.org/3/library/fileinput.html
# Code adapted from Week 7 lecture to open a file and from website
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Opens the python sys module
# Code verbatim from Week 9 lecture example of command line arguments in python
import sys

# Test to check if number of arguments supplied is = 2
# Code adapted from Week 9 lecture example
if len(sys.argv) != 2:
    # print error message and the program does nothing
    print("INPUT ERROR: You should supply a single filename for input.")
else:
    # Otherwise do the following
    # Open the file at the second argument called on the command line
    # i.e. the text file as read only
    # The formated code with {} refers to the second argument of the python
    # list on the command line do the open command opens the first file after
    # python second.py ... on the command line.
    # Code adapted from Week 7 and 9 lectures
    with open(f'{sys.argv[1]}', 'r') as f:
        # For each line in file f read the line
        for line in f:
            # Remove additional line breaks
            # Code adapted from Week 7 lecture
            line = line.rstrip("\n")
            # check for start of every second line, starting with first line as 0
            # The 2 below can be changed to 3, 4, etc. if every third, fourth, etc.
            # lines are needed
            if i % 2 == 0:
                # print the every second line starting with the first line
                print(line)
            # increment i
            i += 1
    # closes the file f
    f.close()
