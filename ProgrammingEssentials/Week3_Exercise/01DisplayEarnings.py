# Question 1. Write a function named DisplayEarnings, with two parameters
# representing an employee's salary and the number of years they have worked.
# This method should dispay their total earnings on the console when invoked.

def DisplayEarnings(salary, years):
    totalEarnings = salary * years
    print("The employees toal earnings are: " + str(totalEarnings))

DisplayEarnings(10000, 5)
