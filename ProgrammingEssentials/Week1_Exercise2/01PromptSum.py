# Week 1 Exercise 2
# Exercise 1: Write a program that prompts the user to enter two integer
# values. The program then increments the first integer by 1 and calculates
# and displays the sum of the both

# Prompt for values
num1 = input("Type in the first integer: ")
num2 = input("Type in the second integer: ")

# Add 1 to the first integer
num1 = int(num1)+1

# Add the values and display
sum = num1 + int(num2)
print("The result is: " + str(sum))
