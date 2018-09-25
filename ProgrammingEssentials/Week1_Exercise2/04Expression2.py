# Week 1 Exercise 2
# Exercise 4: Declare two variables and initialise them both with
# integer values. Write a python expression for ab^2 and display the result.
# prompt for a, b, c, d, and r.

# Input the data
a = input("Please enter value for a: ")
b = input("Please enter value for b: ")
c = input("Please enter value for c: ")
d = input("Please enter value for d: ")
r = input("Please enter value for r: ")

# Change these all to floats
a = float(a)
b = float(b)
c = float(c)
d = float(d)
r = float(r)

# Complete the calulation
result = (4/(3*(r+34)))-9*(a+b*c) + 3 + (d*(2+a))/(a+b*d)

# Return the result as a string
print("The result is : " + str(result))
