###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Sample Exam September 2017                                                  #
# Question 3                                                                  #
###############################################################################

# QUESTION 3
# Write a Python program which accepts a row of delimited data and the
# delimiter used and writes out the individual data fields to the screen as
# per Figure 2 below.

# ######################################
# WELCOME TO THE DBS CONSOLE
# ######################################
# Enter your data row: Ken Collins#Green Street#Cork City#Co. Cork
# Enter your delimiter: #
#
#
# The individual data values are as folows:
# Ken Collins
# Green Street
# Cork City
# Co. Cork

# Again we need to print the intro, lets just copy the code from the earlier
# question.

print("######################################")
print("WELCOME TO THE DBS CONSOLE")
print("######################################")

# Next we need the input, this will be a string data type
userInput = input("Enter your data row: ")
userDelimiter = input("Enter your delimiter: ")

# To split a string based on a dividing character we use the split function
# which returns a list with the string broken up into multiple chunks
userInputList = userInput.split(userDelimiter)

# Fially we need to print this out. The easiest way is to just use a for loop

for item in userInputList:
    print(item)
