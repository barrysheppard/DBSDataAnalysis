###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Sample Exam September 2017                                                  #
# Question 2                                                                  #
###############################################################################

# QUESTION 2
# Create a Function in Python to calculate the sum of the individual digits of
# a given number passed to it as a parameter. See Figure 1 below as an example.

# ######################################
# WELCOME TO THE DBS CONSOLE
# ######################################
# Enter a number: 678
# The sum of the digits of the number 678 is : 21

# Lets start by printing off that message.
print("######################################")
print("WELCOME TO THE DBS CONSOLE")
print("######################################")

# next we need to input the number
userNumber = input("Enter a number: ")
# As we're not doing any error checking, if the user inputs a non-number we
# will get an error. I don't believe including error checking is a requirement
# for full marks.
# If we wanted to we could include this in a loop and keep asking until the
# user enters a number. We need to assign a blank str value first.
# userNumber = ""
# while userNumber.isnumeric() is not True:
#    userNumber = input("Enter a number: ")

# We need to split this into each character, there are lots of different ways
# you can do this but I'm just going to use a simple loop

# I'll start with the result as 0 and I'll add each digit to it one at a time
result = 0
for numberCharacter in userNumber:
    result = result + int(numberCharacter)

# finally we need to print the result
print("The sum of the digits of the number", userNumber, "is :", int(result))
