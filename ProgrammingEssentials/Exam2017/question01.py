###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Sample Exam September 2017                                                  #
# Question 1                                                                  #
###############################################################################


# a. Outline how the following statement is evaluated and state what value x
# is initialised to:
x = 64 / 2 ** 2 + (8 - 7)

#  All operators except the power (**) operator are evaluated from left to
# right and are listed in the table from highest to lowest precedence. That is,
# operators listed first in the table are evaluated before operators listed
# later. (Note that operators included together within subsections, such as
# x * y, x / y, x // y, and x % y, have equal precedence.)
# http://www.informit.com/articles/article.aspx?p=459269&seqNum=11
# x evaluations as 17. 64 / 4 + 1


#  b. What is the output from the following code:
def CalculateDogsAgeInDogYears(humanYears):
    if humanYears < 0:
        return None
    elif humanYears <= 2:
        return(humanYears * 10.5)
    else:
        return(21 + (humanYears - 2) * 4)


print(CalculateDogsAgeInDogYears(-1))
print(CalculateDogsAgeInDogYears(0))
print(CalculateDogsAgeInDogYears(5))
print(CalculateDogsAgeInDogYears(11))
print(CalculateDogsAgeInDogYears(20))

# Results
# None
# 0.0
# 33
# 57
# 93
#
# Note that Python will assume numbers are int if they don't have a decimal
# In this case the * 10.5 operation changed the 0 to 0.0 as it changed from
# an int to a float.


# c. The following code results in an error message. What will the error
# message be and how can it be fixed?
def addOne(n): n=n+1
return n


# The error message is: File "<string>", line 4 SyntaxError: 'return' outside
# function
# The problem here is the return should be intended so python knows it is
# part of the function. If you have a short function you could have it on the
# same line, but that n=n+1 should really be on the next line also.
# Fixed code looks like this.
def addOne(n):
    n = n+1
    return n


# d. Identify which of the following lines of code will never not get executed:
def divideMe(j):
    k = j - (2/0)
    if (k <= 6):
        return 6
    else:
        return k


j = 5
divideMe(j)

# The function will be defined. The j = 5 will run, the divideMe(j) will run
# but will result in an error. In the function the first line of k = j - 2/0
# will cause a ZeroDivisionError: division by zero. Everything below that line
# in the function will not run.

# e. What is the output from the following:
j = 7
k = 3

print(k * j + 1)
j = (j + 1)
print(j + 1)
k = (j + 1 + k)
print (k + 1)

# When using print statement we need the variables as strings, in a case like
# where all the variables are int the code is smart enough to calculate the
# final number and convert it to a str automatically.
# As these are all numbers it treats the * and + as number operators.
# If j or k were a string, the + would be treated as a concatenate (join)
# operator and would result in a TypeError: must be str, not int as the 1 is
# a number. If both were strings this would join them together with no space
# in between. If we used a comma seperated in the print line print(k,j) this
# would include a space between the two variables.


# f. What is the output from the following:
a = 0
b = 2
print("Begin")
while a < 0 + 1:
    print("Middle")
    a = b
print("End")

# Begin
# Middle
# End
#
# The print("Begin") line will run as theres no reason not to.
# The first time the while loop runs a will be 0 which is les than 0 + 1
# a is then set to b which is two.
# Look out for loop like this where there is an and or an or, as this will make
# the logic a little tricker to work out.
# the second time the while loop attempts to run, a will be 2 which is greater
# than 0 + 1 so the loop will not run again.
# then the last print("End") will run, as it is outside of a loop and this is
# the last line, no more runs.


#g. What is the output from the following:
def addNumbers(a, b):
    try:
        return a + b
    except Exception as e:
        return -1


print(addNumbers("", 10))
print(addNumbers(29, 5))
print(addNumbers(50, -10))
print(addNumbers(-5, ""))

# Output is
# -1
# 34
# 40
# -1
# In the first and last call there is a blank str. This means the code will
# generate a TypeError: unsupported operand type(s) for +: 'int' and 'str'
# As the function has exception handling, this will be 'sunk' and instead the
# code returns -1 as the result as per the except line.

# h. Where is the finally keyword used in Python and why would you used it.
# Give an example to support your answer.

# Finally is used after a try, except piece of code to have a piece of code
# that will always run regardless of whether the try succeeds or fails.
# An example would be a database connection where you want to close the
# connection regardless of whatever happens.

try:
    [code to connect to database]
    [code to amend an entry on the database]
except Exception as ex:
    raise ex
finally:
    [code to close connection to database]


# i. What is the output from the following:
x = -7
y = 22
result1 = (x > y) or (y < 12)
result2 = ((x == 0) and (y != 0)) or (y != x)
result3 = (y == 10) or (x % y != 0) and (x != y)
result4 = (y >= x+10) and (x == 0) and y != 15
result5 = not (y - x == 10) and (x < y)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

# As these are all logic, the result is going to be True or False
# resolve left to right one piece at a time.
# False  # (-7 > 22) or (22 < 12). As the first is true this resolves as true
# True  # again a or statement, only 1 needs to  be true. 22 is not = 0 is true
# True  # (22 == 10) or (-7 remainder 22 is not 0) and -7 is not 22
# False # (22 is >= -7 + 10) and (-7 is equal 0) and 22 is not equal to 15
# True = not (-7-22 equals 10) and (-7 <22)


# j. Take below class definition. Extend the class to have a function named
# PrintBalance which prints out the output “Account Id 101 has a current
# balance of : 50.00”

class Account:
    __accountId = 101
    __type = "Loan Account"
    __balance = 50.00

    def PrintBalance(self):
        printString = "Account Id " + str(self.__accountId)
        printString = printString + " has a current balance of : "
        printString = printString + str(self.__balance)
        print(printString)

# functions in a class are actually called methods, but moving on from that
# we use self as an argument for the function so it knows where to get the
# variables. This is needed as the variables are outside the function in the
# class.
# In this case as the string is so long I've joined it up one step at a time.
# The + symbol when used with strings means concatenate (join up). Unlike when
# we use comma in the print statement, this doesn't add spaces, so we need to
# make sure they are at either side of the text. As the numbers are currently
# in the int type, we need to use str() to convert them or we will get an error
