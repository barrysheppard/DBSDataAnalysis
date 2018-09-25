###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Sample Exam September 2017                                                  #
# Question 4                                                                  #
###############################################################################

# QUESTION 4
# Write a program in Python which is a Menu-Driven Program to perform a simple
# calculation as per below example in Figure 3.

# ######################################
# WELCOME TO THE DBS CONSOLE
# ######################################
# Enter the first number: 15
# Enter the second number: 10
#
#
# MENU OPTIONS
# 1-Addition
# 2-Subtraction
# 3-Multiplication
# 4-Division
# 5-Modulus
# 6-Exit
#
# Enter menu choice: 5
# The Modulus of 15 and 10 is 5
# Press any key to continue...

# Note that the last line is the end of the program so this doesn't have to be
# an infinite loop. Just in case, it's worth mentioning this in the code
# comments just in case the lecturer didn't realise.

# Start by printing. As a change we're going to use triple quotes. This lets us
# include line breaks which will make it a little easier to write.
print("""######################################
WELCOME TO THE DBS CONSOLE
######################################""")

# Lets get the two user numbers
userNumber1 = input("Enter the first number: ")
userNumber2 = input("Enter the second number: ")
# As before we're not using any numeric validation but if we had extra time
# at the end and wanted to show off we could with userNumber1.isnumeric()

# Next lets churn out that big block of options. Note the blank lines at
# the start. Again we use the triple quotes to save time but you could do
# individual print commands for each line.
print("""

MENU OPTIONS
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Modulus
6-Exit
""")

# As the user for their choice
userChoice = input("Enter menu choice: ")
# Again if we wanted we could add a loop to make sure the user adds a valid
# choice. In this case we're just going to add an else message to handle any
# invalid selection.

# The value we return is based on the user choice.
# We're just going to work out the final result and record the type of
# operator we used, we can combine this into the output at the end

# After doing this the first time I noticed the phrasing was a bit weird
# so I've gone back and added a join variable.
if userChoice == "1":  # Remember this is still a string
    operator = "Addition"
    join = " and "
    result = int(userNumber1) + int(userNumber2)
elif userChoice == "2":
    operator = "Subtraction"
    join = " minus "
    result = int(userNumber1) - int(userNumber2)
elif userChoice == "3":
    operator = "Multiplication"
    join = " by "
    result = int(userNumber1) * int(userNumber2)
elif userChoice == "4":
    operator = "Division"
    join = " by "
    result = int(userNumber1) / int(userNumber2)
elif userChoice == "5":
    operator = "Modulus"
    join = " mod "
    result = int(userNumber1) % int(userNumber2)
elif userChoice == "6":
    exit = True
else:
    print("You selected an invalid choice")
    exit = True

# Check if we need to print something, and if we do print it.
if exit is not True:
    # We've broken this up over multiple lines to make it easier to read
    userOutput = "The " + operator + " of " + userNumber1 + join
    userOutput = userOutput + userNumber2 + " is " + str(result)
    print(userOutput)
