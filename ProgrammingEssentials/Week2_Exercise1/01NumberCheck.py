# Write a program which reads two integer values. If the first number is
# less than the second, print the message "First number is less that the
# second". If the second is less than the first, print the message "Second
# number is less than the first". If the numbers are equal, print the message
# "The numbers are equal"

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

if num1 < num2:
    print("First number is less than the second")
elif num1 > num2:
    print("Second number is less than the first")
else:
    print("The numbers are equal")
