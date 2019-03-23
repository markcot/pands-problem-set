# Exercise 9 - second.py
# Mark Cotter, V1_02, 2019-03-23

# V1_02 - 2019-03-23
# Code added to print every second line of the text

# V1_01 - Program created 2019-03-22

# A program that reads in a text ﬁle and outputs every second line. The program
# takes the filename from an argument on the command line.

# Input file for reading
# Code adapted from website
# https://stackoverflow.com/questions/7033987/python-get-files-from-command-line

# variable counter i
i = 1
# variable f is for the file name loaded
# variable line is for reading each line in the file f

# Opens a file moby-dick.txt from the current folder
# Code adapted from Week 7 lecture to open a file and from website
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
with open('moby-dick.txt', 'r') as f:
    # For each line in file f print the line
    for line in f:
        # Remove additional line breaks
        line = line.rstrip("\n")
        # check if line is odd (every second line)
        if i % 2 != 0:
            # print the every second line
            print (line)
        # increment i
        i += 1
# closes the file f
f.close()
