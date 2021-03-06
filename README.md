# pands-problem-set
## GMIT problem set for Programming and Scripting Module 2019
#### Created by: Mark Cotter, Email: g00376335@gmit.ie
### LAST UPDATED 2019-03-30

#####################################################################################

## Exercise 1 - sumupto.py
Using python code
Requests user to enter a positive integer 'i'
The 'sum' of numbers between 1 and the entered value of 'i' is outputted

### 2019/02/01
I created the first file 'python sumupto.py' version V1_01 in a folder on my Desktop.
My first thought was that I needed to have variables for the user to
enter save a positive integer and to save a sum in.
I created the variables 'i' and 'sum' and gave them initial state values.

I didn't know how to ask python how to request a user to input something so
I did a google search and found the website
https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
I adapted the code on the page for the 'input()' function and the data type
'int' so that the program requested the user to enter an integer.

I found that as I specified an integer type input, if the user entered a string 
or float the program would automatically give an error so I decided that I didn't 
need to write a test loop if the number entered was not an integer.
However I didn't want a negative or zero integer so I wrote a loop to give an error
message if a number less than 1 was entered and to keep requesting a positive integer.

I wanted to keep the variables used to a minimum so I did not want to use a counter
variable as discussed in the GMIT January 2019 lecture notes. Instead I decided that as 
I didn't need to output the value of the entered variable 'i' at the end of the
program, I could just use a loop to count down from the value of 'i' to 0 and keep adding
the value of 'i' to the total variable 'sum'.

I added extra print functions to the code, to test what happened to variables when 
I made tweets to the code. At the end I just added # before these print functions so
they would not print in the final version of the code, but could be used later if
the code needed to be amended.

To get my head around a bit of the code and function I did some reading of the book
'A Whirlwind Tour of Python': VanderPlas, Jake: published by O'Rielly Media Inc. 2016
From the code example in the book and GMIT Jan 2019 lecture noted I adapted shorted
version of adding the sum to itself and operators '+=' and '-='.

I got the program working and called it a day.

### 2019/02/02
I updated the file 'python sumupto.py' to version V1_02 in my Desktop folder
I was interested to see if I could use a range function to solve this problem rather
than using a while loop. After playing around with it for a while, I found that for the
range function to work I needed an extra variable to cycle through the values out of the range. I added a variable 'x' and gave it it an initial value.
I added double comment markers ## to the OPTION 01 while loop while I tested the 
OPTION 02 range function.

I wanted the range function to start at 1 and end at the value of
the entered variable 'i'. However I needed to add +1 to 'i' for this to work so using the
'range of 1 to (i+1)' gave me the desired result. Using x in this range and the 
'for' function I was able to calculate the 'sum' without looping.
I wasn't sure which would be a more efficient use of the program not having the while loop or having 2 or 3 variables. I decided to stick with OPTION 01 while loop that had only 2 variables, but changed the value of 'i' and comment out ## the OPTION 02 for loop with 3 variables, but retained of value of 'i'. I left instruction in comments that if the value of 'i' need to be retained the OPTION 01 while loop could be commented out (add ## before code) and the OPTION 02 for loop and 'x' variable could be uncommented (remove ## before the code)

I created my github profile and added 'python sumupto.py' version V1_02 to the
repository. At the time I didn't know about typing a commit message so first commit
was missing a message.

### 2019/02/09
As advised by Ian, I decided to create this README.md file and updated the file 'python sumupto.py' to version V1_03 amended some comments and added notes to my references

### 2019/02/10
Updated the file 'python sumupto.py' to version V1_04 & amended some comments

### 2019/02/17
Updated the file 'python sumupto.py' to version V1_05 & amended some comments

### 2019/03/30
I decided to add an exception check for the correct input type value
as discussed in the Week 10 lecture notes.

I removed the option 02 with the 'x' variable from the code.
I remove the int() from input() request function so that I could check later check
if the inputted value was correct, without having to loop a continuous request for a
new value for 'i'

If the inputted value for 'i' is not the correct integer type a TYPE error message
is displayed and the program does not compute anything.
If the inputted value for 'i' is not a non-zero positive integer an VALUE error
message is displayed and the program does not compute anything.

Version V1_06 of the program created and uploaded to github.

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   January 2019
   I adapted the lecture notes while loop to count down to 0 from i so
   that I could leave out a counter variable

2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
   published by O'Rielly Media Inc. 2016
   Reading first few chapters I adapted shorted version code for adding
   the sum to itself and operators '+=' and '-='

3. I adapted code on the following web page to request user to input a value
   and make that value an integer.
   https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html

4. I adapted code from Week 10 lecture in relation try and except for exceptions.

#####################################################################################

## Exercise 2 - begins-with-t.py
Using python code
Check if today is a day that begins with the letter 'T'
(i.e. 'Tuesday' or 'Thursday')
Outputs 'Yes' if today begins with a 'T'
Outputs 'No' if today does not begin with a 'T'

### 2019/02/02
I created the first file 'begins-with-t.py' version V1_01 in a folder on my Desktop
My first thought was that I could possibly adapt code from the Jan 2019 GMIT lecture
example Python-Tuesday to suit this problem.

I created a variable 'today' for today's date.
I began playing with the idea that if I could write an if and elif
statements using code 'if datetime.datetime.today().weekday() == 1:' for Tuesday
and 'if datetime.datetime.today().weekday() == 4:' for Thursday. I could make the Yes
condition print if either of these conditions were true and use an else function to
print No.

I added extra print functions to the text to test what happened to variables when 
I made tweets to the code. At the end I just added # before these print functions so
they would not print in the final version of the code, but could be used later if
the code needed to be amended.

However, I thought that this was a boring solution and wanted to shorten it. I noticed
that the problem was really to check if today starts with the letter 'T'. I wondered
if I could find a function to return the current day of the week as a text string.
I did a google search and found the following website and adapted some of the code to
return a string for the current day of the week
https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

I found that if I added the string date type to the function it get the variable 'today' as a text string with todays date. Now I need to extract the first letter from this string.
I did a google search and found the website.
https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list
I adapted the code on the webpage to select the first character of the text string 'today'

I created an if and else function to test of 'today' begins with a 'T'.

The revised version of the program worked a treat.

I created my github profile and added 'begins-with-t.py' version V1_01 to the
repository. At the time I didn't know about typing a commit message so first commit
was missing a message.

### 2019/02/09
As advised by Ian, I decided to created this README.md file and updated the file 'begins-with-t.py' to version V1_02 amended some comments and added notes to my references.
On thinking back maybe 'today' wasn't a good variable name for this program as I have
read that 'today' may already be defined variable in programming. After more 
research, I may change this variable name at a later date.

### 2019/02/10
Updated the file 'begins-with-t.py' to version V1_03 & amended some comments

### 2019/02/17
Updated the file 'begins-with-t.py' to version V1_04 & amended some comments

### 2019/03/30
Updated the file 'begins-with-t.py' to version V1_05 & amended some comments

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   January 2019
   I adapted code from the lecture notes example Python-Tuesday for checking
   what todays day of the week is.

2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
   published by O'Rielly Media Inc. 2016
   Reading first few chapters I adapted code for if and elif for use in this
   program.

3. I adapted code from the following webpage to return a string for the
   current day of the week
   https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

4. I adapted code from the following webpage to return the first character
   of a text string. This was covered also in a later GMIT lecture
   https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list

#####################################################################################

## Exercise 3 - divisors.py
Using python code
Write a program that prints all numbers between 1,000 and 10,000
that are divisible by 6 but not 12

### 2019/02/10
I created the first file 'divisors.py' version V1_01 in a folder on my Desktop
that is now linked using git to my github repository 'pands-problem-set'.

My first thought was that I could possibly adapt code from the Jan and Feb 2019 GMIT
lectures for lecture notes example of for loops and remaining fractions after
divisions (modulus) and to print numbers when the modulus == 0 after division.

I wanted this program so that it could be modified later to look for other divisors.
As such, I decided that rather than hard coding the numbers 6 and 12 into the code, 
I would use two variable 'a' and 'b' for the values of 6 and 12 at the start of the
program so that they could be easily changed later on. Also maybe it would be good
to have two variables to use for range 1,000 and 10,000 so these could also be changed
later in a modified version of this program. Also I wanted a variable to search in the range of 's' to 'e'.

I created 5 variable 'a', 'b', 's', 'e' and 'x' for 'lower divisor' of 6, 'upper divisor'
of 12 in the range 'starting' at 1,000 and 'ending' at 10,000 with 'x' to search the
range. I also wanted to use the multiple assignment and line break '/n' print statement, I
learned in the GMIT week 3 lecture videos.

I wrote a temporary print statement check what the divisors and range would be.
Afterward I added a # to comment out the print statement, while saving it for later.

I wrote a for loop to check if to check values in range 's' to 'e' fulfil the
TRUE condition = "divisible by 'a' but not by 'b'"
I used 'x' to search the range and print the number when the required condition
TRUE. The end of the range has to extended by +1 to ensure that the value of 'e'
is also checked for the TRUE condition.

The program works. I spot checked few of the output values and all the values I check
were divisible by 6 ('a') but returned a 0.5 remainder when divided by 12 ('b').
I added 'divisors.py' version V1_01 to git and uploaded to my github repository.

### 2019/02/17
Updated the file 'divisors.py' to version V1_02, amended some comments
and if statement '&' replaced with 'and'. Changed variable 'x' to 'i'

### 2019/03/30
Updated the file 'divisors.py' to version V1_03, amended some comments

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   January and February 2019
   I adapted code from the lecture notes example of 'for' loops and remaining
   fractions after divisions and to print numbers when modulus = 0 after division
   I also adapted code for print statement over multiple line "\n"

2. 'A Whirlwind Tour of Python': VanderPlas, Jake:
   published by O'Rielly Media Inc. 2016
   Reading first few chapters I adapted code for modulus if and elif for use
   in this program.

#####################################################################################

## Exercise 4 - collatz.py
Using python code
Write a program that
1. Asks a user to input any positive integer and
2. Outputs the successive values of the following calculation
3. At each step calculate the next value by taking the current value and
4. if it even, divide it by 2 
5. but if it odd, multiply it by three and add one
6. End the program when the current value it one.

### 2019/02/10
I created the first file 'collatz.py' version V1_01 in a folder on my Desktop
that is now linked using git to my github repository 'pands-problem-set'.

My first thought was that I could possibly adapt code I wrote for Exercise 1
'sumupto.py' to ask user for a positive integer. That cover part 1 of the program
Also i could use part of the modulus part of the code from Exercise 3 'divisors.py'
to check if the calculated value is even or odd by checking the modulus after 
dividing by 2 is = 0

As with 'sumupto.py' I found that as I specified an integer type input, if the
user entered a string or float the program would automatically give an error 
so I decided that I didn't need to write a test loop if the number entered was 
not an integer.
However I didn't want a negative or zero integer so I wrote a loop to give an 
error message if a number less than 1 was entered and to keep requesting a 
positive integer.

I figured the best way to save this calculated data was to create a list and keep
using the last digit in the list to cycle through the list and keep appending the
data to the end of the list. This way I could print the list at the end of the 
program

I created a variable 'i' to store the inputted and apply the
calculation to. I created a list 'l' to store the calculated values in and to
print at the end.

I adapted code from the python online tutorial webpage
https://docs.python.org/3/tutorial/introduction.html#lists and
https://docs.python.org/3/tutorial/datastructures.html
I created a while loop to apply the required calculation to 'i' until 'i' = 1
In each loop I used the list.append(i) command to add the value of 'i' to the
end of the list and checked last value in the list to see if it equals 1.

The program worked, but the output was a in a list format if the print(l) command was
used. eg for starting at integer 10, output is [10, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
I noticed that the output of the even number division was a float instead of integer.
I added the i = int() function in the previous loop to force the even number division
into an integer. I think the float division // may have had the same effect.

I then needed to extract the values from the list 'l' and print them in a line
to get the same text as shown in the exercise.
I adapted code from the python online tutorial webpage
https://docs.python.org/3/tutorial/introduction.html#lists
in a 'while' loop to create a 'for' loop to print all the values in the list 'l' with
a space separator only print( , end=' ')

The program works. I added 'collatz.py' version V1_01 to git and uploaded to my github repository.

I updated the file file 'collatz.py' version V1_02 & updated some of the comments and
uploaded it to my github repository.

### 2019/02/17
Updated the file 'collatz.py' to version V1_03 & amended some comments

### 2019/03/30

I remove the int() from input() request function so that I could check later check
if the inputted value was correct, without having to loop a continuous request for a
new value for 'i'

If the inputted value for 'i' is not the correct integer type a TYPE error message
is displayed and the program does not compute anything.
If the inputted value for 'i' is not a non-zero positive integer an VALUE error
message is displayed and the program does not compute anything.

Amended some comments and updated the file 'collatz.py' to version V1_04

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   January and February 2019
   I adapted the lecture notes while loop and discussion about lists
   and the appending items to lists.

2. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' and Exercise 3
   divisors.py asking user to input a positive integer check if it even or odd
   by checking the modulas after dividing by 2 is = 0

3. 'A Whirlwind Tour of Python': VanderPlas, Jake:
   published by O'Rielly Media Inc. 2016
   Reading first few chapters I adapted code for not equal to != if and
   elif for use in this program.

4. I adapted code from the following python tutorial webpage about lists
   and appending list. I adapted code in a 'while' loop to create a 'for' loop
   to print all the values in the list 'l' with a space separator only
   print( , end=' ')
   https://docs.python.org/3/tutorial/introduction.html#lists
   https://docs.python.org/3/tutorial/datastructures.html

5. Code adapted from Exercise 1 - sumupto.py and Week 10 lectures for checking
   for inputted values with try and except functions

#####################################################################################

## Exercise 5 - primes.py
Using python code
Write a program that asks the user to input a positive integer and tells the
user whether or not the number is a prime.

### 2019/02/17
I created the first file 'primes.py' version V1_01 in a folder on my Desktop
that is linked using git to my github repository 'pands-problem-set'.

My first thought was that I could possibly adapt code I wrote for Exercise 1
'sumupto.py' to ask user for a positive integer. That cover part 1 of the program.
I used this code to ask the user for a number and stored it in the variable 'num'
As with 'sumupto.py' I found that as I specified an integer type input, if the
user entered a string or float the program would automatically give an error 
so I decided that I didn't need to write a test loop if the number entered was 
not an integer.
However I didn't want a negative integer so I wrote a loop to give an 
error message if a number less than 0 was entered and to keep requesting a 
positive integer until 0 or greater positive integer.

In the Week 4 lecture notes, there was a discussion about the break keyword
and using for loops to check for primes so that seemed like a good place to start.
I noticed that the scope of the program was to just tell the user if the
number was a prime. Therefore, the program shouldn't do anything if the positive
integer is not a prime.

The first prime number is 2 so if a 0 or 1 is entered, the program should also
does nothing. If the number inputted is 2 or greater check if the number a prime
by check if is has any divisible number between 2 and up the number. 

The program cycle through the range of values between 2 and 'num'. I used a variable 'i' cycle through the range.

The program works. I added 'primes.py' version V1_01 to git and uploaded to my github repository.

### 2019/03/30 (a)
I remove the int() from input() request function so that I could check later check
if the inputted value was correct, without having to loop a continuous request for a
new value for 'num'.

If the inputted value for 'num' is not the correct integer type a TYPE error message
is displayed and the program does not compute anything.
If the inputted value for 'num' is not a positive integer an VALUE error
message is displayed and the program does not compute anything.

I added print statements if the positive integer inputted is not a prime.

Amended some comments and updated the file 'primes.py' to version V1_02

### 2019/03/30 (b)
Amended some comments and updated the file 'primes.py' to version V1_03

### 2019/03/30 (c)
Amended some comments and updated the file 'primes.py' to version V1_04

## Code reference sources:
 1. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' asking user
    to input a positive integer.
    
 2. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
    January and February 2019
    I adapted the lecture notes code about for loops and break 

 3. I adapted code from the python online tutorial webpage
    https://docs.python.org/3/tutorial/controlflow.html 
    to use a for loop and break to check if a number is a prime

 4. Code adapted from Exercise 4 - collatz.py and Week 10 lectures for checking
    for inputted values with try and except functions

#####################################################################################

## Exercise 6 - secondstring.py
Using python code
Write a program that takes a user input string and outputs every second word.

### 2019/03/20
I created the first file 'secondstring.py' version V1_01 in a folder on my Desktop that is linked using git to my github repository 'pands-problem-set'.

My first thought is store the string and to split is into an list using the
str.split() from Week 7 lecture notes.
Then use a while loop to cycle through every second item in the list
and print the result.
The sentence could be long so I'll it the length open ended.
I have to specify that the separator as a white space character.
I will assume that I will not have to check if the text entered and not
have to check if it is a integer or float type.
I may have to strip full stops and commas to get the program to work

From the following website, I found that it is better to replace commas
in the string rather than striping them
https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string

To split the sentence into an list I used code referenced in GMIT H Dip Data
Analytics lecture video Week 7 - March 2019 &
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

As with Exercise 4 - collatz.py I used the same code to print the result list 'r'
in a single line.

I taught I might be able to remove one of the loops at the end by adapting the
while loop into a for loop. This would also use one less variable. This change worked
and I was able to remove the list 'a'.

I did notice during testing that if a float number is entered such as 1.0,
the point is removed from between the 0 and 1, but as this program is for
sentences I did not think that this issue needed to be addressed.

I deleted the unused code, saved the file and made the last commit for version
V1_01 of 'secondstring.py'.

### 2019/03/30
Amended some comments and updated the file 'secondstring.py' to version V1_02

## Code reference sources:
1. Mark Cotter February 2019 code for Exercise 1 'sumupto.py' asking user
   to input a positive integer or string. 

2. Code for replacing commas and full-stops adapted from website 
   https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string

3. Code for spliting the sentence into an list adapted from GMIT H Dip Data
   Analytics lecture video Week 7 - March 2019 & website
   https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

4. Mark Cotter February 2019 code for Exercise 4 - collatz.py' for print from
   an list onto one line.


#####################################################################################

## Exercise 7 - squareroot.py
Using python code
Write a program that that takes a positive ﬂoating point number as input and
outputs an approximation of its square root.

### 2019/03/21
I created the first file 'squareroot.py' version V1_01 in a folder on my Desktop that is linked using git to my github repository 'pands-problem-set'.

First I need to ask a user to input a positive floating point number
Then I need to check that the number is positive, >= 0
I could reuse some code modified from the previous exercises to achieve this.
I did not create a loop for checking if a non-number text was entered by the
user, but this could be added later if needed. 
I was thinking of defining a function to ask the user for the input so that
I would have to write less code when checking what the user input is acceptable,but the amount of code is less for not using a function in this case.

To calculate the square root I was thinking of using the power function 
x = 9, x ** 0.5 which would give the square root, but this would give the exact
square root of the number. I was thinking about it for a while and was
wondering if I could guess a number less than the inputted number. By dividing
the the guess into the inputted number, using a loop I could try and get a 
better approximation of the number.
In the week 8 lecture, using Newton's method was discussed, which looked like
a good method for calculating the square root. I did some searching online
and came across another version of Newton's method called the 
Babylonian square-root algorithm on webpage
https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

S = any positive number
To find the square root of S, you need to make an initial guess
x0 = first guess
x1 = next improved guess using the formula
x1 = (x0 + S/x0)/2

I decided to try the Babylonian square-root algorithm method and use the
inputed number divided by 2 as the first guess.

I noticed that the problem asks for the approximate square root and only
one decimal place is shown. As such I decided to print resulting square
root to one decimal place only. The website highlight the python round function
https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830
This website also discusses the fact the round() function does not round 
correctly
E.g. 'round(55.15,1)' is rounded to 55.1, but it should round up to 55.2
     'round(55.16,1)' is rounded to 55.2
However for an this approximation of square root, this level of accuracy is
acceptable.

I will use 'num' as the variable for the entered number and 'root' as the
variable for the approximation of the square root of 'num'

### 2019/03/30
I remove the float() from input() request function so that I could check later check
if the inputted value was correct, without having to loop a continuous request for a
new value for 'num'.

If the inputted value for 'num' is not the correct number type a TYPE error message
is displayed and the program does not compute anything.
If the inputted value for 'num' is not a positive number an VALUE error
message is displayed and the program does not compute anything.

I added print statements if the positive integer inputted is not a prime.

Amended some comments and updated the file 'squareroot.py' to version V1_02

## Code reference sources:
1. Code adapted for Babylonian square-root algorithm found on webpage
   https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

2. Code adapted from Exercise 5 - primes.py and Week 10 lectures for checking
   for inputted values with try and except functions

3. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   I adapted code from the Week 8 lecture for looping a square root

4. Code for rounding number to one decimal place adapted from website
   https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830

5. Formated print statement code adapted from Week 7 lecture.



#####################################################################################

## Exercise 8 - Datetime.py
Using python code
Write a program that outputs today's date and time in the format
"Monday, January 10th 2019 at 1:15pm".

### 2019/03/21
I created the first file 'Datetime.py' version V1_01 in a folder on my Desktop that is linked using git to my github repository 'pands-problem-set'. I had to rename
the file with a capital D as the lower case datetime is already a function, so I
couldn't call the function datetime in the script and call the file datetime.py as
the name.
I found out from the following website that there is an issue with datetime being
both the module name and module class.
https://stackoverflow.com/questions/15707532/python-import-datetime-v-s-from-datetime-import-datetime
I imported the datetime module and use the abbreviation 'dt'

My first thought was to use some of the datetime functions highlighted in Week 6
lecture and on the Python online library
https://docs.python.org/3/library/datetime.html for printing the various format
year month day and time based on the datetime module and used in Exercise 2 -
begins-with-t.py

I got the program working, but I found 2 problems 
1) Getting the st, nd, rd or th to display after the day for 1st, 2nd, 3rd, 4th, etc.
2) To get the PM after the minutes to display as lower case and removing the leading
   zero from the hour.

I may need a few if loops prior to the printing the information

### 2019/03/22 (a)
I updated the program to version V1_02
The following websites have a few methods of adding the day suffix st, nd, rd or th
https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime

https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like

The following website has some ideas on changing the pm/am time to lower case and
removing the leading zero from the hour. (Get “2:35pm” instead of “02:35PM”)
https://stackoverflow.com/questions/2925230/get-235pm-instead-of-0235pm-from-python-date-time

The following webpage also has a guide for the datetime function strftime
https://linux.die.net/man/3/strftime
However the lowercase function "%P" for pm/am does not appear to work for me.

I think it is best to split up the time into separate string variables. Manipulate
the text as needed and print the result as formated string.
I convert the day of the month and hour into integers to remove the leading zeros
and to check what suffix I needed to add to the end of the day of the month.
For the if loop checking the day of the month,I found that the or between the number
did not give the desired result, (1 or 21 or 31), but the or symbol | did.
I must investigate this further.

### 2019/03/22 (b)
I updated the program to version V1_03
I changed the format of the if and elif checking for the suffix of the day of the
month, because further testing should that the desired result was not printing
correctly of a number of different day of the month. The if statements were only
looking at the first number in the line '1 or 21 or 31' and was not checking the
other options correctly. As there were only a few combinations I wrote if or elif
statements of each of the alternative values 1, 2, 3, 21, 22, 23 and 31. The other
numbers in the month all have the suffix 'th'.
Final issue upload to Git hub.

### 2019/03/23
Variables initial values added and minor comments added version V1_04 created.
Code rearranged to make easier to read.

### 2019/03/30
Amended some comments and updated the file 'Datetime.py' to version V1_05.

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   I adapted code from the Week 6 lecture for importing datetime module

2. Code adapted for printing the various year month day and time from webpage
   https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
   and Exercise 2 - begins-with-t.py

3. Code adapted from Week 7 lecture for changing string text to lowercase

#####################################################################################

## Exercise 9 - second.py
Using python code
Write a program that reads in a text ﬁle and outputs every second line. The program
should take the filename from an argument on the command line.

### 2019/03/22
I created the first file 'second.py' version V1_01 in a folder on my Desktop that is linked using git to my github repository 'pands-problem-set'.

I download a section of the first chapter of the moby dick novel from the following
website http://www.gutenberg.org/files/2701/2701-0.txt and saved it my folder as
moby-dick.txt

### 2019/03/23 (a)
First I was thinking about how to load a file from the command line 
Looking at the Python reference website page on file inputs
https://docs.python.org/3/library/fileinput.html
I tried to adapt some of the code from the page to input the file.
I found this website and tried to adapt some code from it.
https://stackoverflow.com/questions/7033987/python-get-files-from-command-line

I found it difficult to figure out how to select the input file directly from the
command line so I decided to come back to the file input part and focus on
outputting every second line of the file for now.
I adapted code from Week 7 lecture for input files from the same folder and remove
additional line breaks and from website
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
I added a counter 'i' and an if statement to only print every second line.

I had to change some of the -- and ' from the downloaded file because python was
reading them as strange looking characters.
Version updated to V1_02.

### 2019/03/23 (b)

Added some additional comments
The 2 in the if statement condition (i % 2 == 0) can be changed to 3, 4, etc.
if every third, fourth, etc. lines are needed.

Using the filename and not specifying a filename within the argument input(), 
python reads the filename given after the program name. This is gives the
desired result and reads the moby-dick.txt entered in the command line after
the program name.
The filename has to be specified after the program name.
I.e. 'python second.py moby-dick.txt'
Otherwise the program will run on an infinite loop

Version V1_03 of the program created and uploaded to github.

### 2019/03/23 (c)

After watching the Week 9 lecture I can see that the sys.argv is a better way of 
reading the mody-dick.txt file into the program so I decided to change the input
method and use the same checking if statement used in Week 9 lecture to check
if only 2 arguments are used when calling up this program second.py.

I note that I had to use the format open command with curly brackets around the
placeholder for the 'sys.argv[1]' for the code to read the text as moby-dick.txt
Now the program does not run an infinite loop if no file name is added after
python second.py on the command line.

Version V1_04 of the program created and uploaded to github.

### 2019/03/30
I decided to add the 'lcount' variable added if needed in future for reading every 
third, fourth or fifth line, etc.

Amended some comments and updated the file 'second.py' to version V1_05.

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   Some code verbatim and other code adapted from the Week 9 lecture for importing
   the sys module and using the sys.argv function and printing Error message and
   closing files.

2. Code adapted for striping additional line break adapted from Week 7 lecture.

#####################################################################################

## Exercise 10 - plotfunction.py
Using python code
Write a program that displays a plot of the functions x, x^2 and 2^x in the
range [0, 4].

### 2019/03/23 (a)
I created the first file 'plotfunction.py' version V1_01 in a folder on my Desktop that is linked using git to my github repository 'pands-problem-set'.

I noticed that the scope is for a single plot with all three function
(x, x^2 and 2^x) shown. Week 9 lecture about matplotlib.pyplot seemed the ideal
for use in this problem. I would have to figure out how to get all three functions
to display on a single plot.

I decided to create an array x in the range 0 to 4, an array s of the square of the
numbers x and an array p for 2 to the power of the numbers in x.
I used a range function to generate x and for loops the content of square of x and
2 to power of x

### 2019/03/23 (b)
I changed the creation method for the x, x^2 and 2^x using the numpy.arange function
I found on webpage https://physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html
This allowed me to generate x^2 and 2^x using simple math formulae.

However, I did noticed a significant slowdown in the run time when I import numpy
ans again when I imported matplotlib.pyplot into python.

I adapted code matplotlib.pyplot.plot function from
https://matplotlib.org/users/pyplot_tutorial.html
to plot the three functions x, x^2 and 2^x and 3 different colours on the
same graph and to give the graph labels.

I adapted code from the following website to edit x axis interval
https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib

Version V1_02 of the program created and uploaded to github.

### 2019/03/30
Amended some comments and updated the file 'plotfunction.py' to version V1_03.

Saved the plotted Figure as 'Figure_1 (plotfunction.py).jpeg' in the git folder

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   Some code verbatim and other code adapted from the Week 9 lecture for plotting
   using matplotlib and numpy modules

2. Code adapted for setting min to max numpy array values from website
   https://physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html

3. Code adapted for ploting using matplotlib from website
   https://matplotlib.org/users/pyplot_tutorial.html

4. Code adapted for add label to x and y axes from website
   https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib





#####################################################################################