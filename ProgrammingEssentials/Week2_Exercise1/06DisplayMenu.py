# Write a program which displays a menu to the user. The menu should look
# similar to the following:
#     Welcome to the SimpleCal
#     Press 1 to add two numbers
#     Press 2 to subtract two numbers
#     Press 3 to divide two numbers
#     Press 4 to multiple two numbers
# Read in the selection from the user and then ask the user for two numbers.
# Print the result to the user.

print("Welcome to the SimpleCal")
print("Press 1 to add two numbers")
print("Press 2 to subtract two numbers")
print("Press 3 to divide two numbers")
print("Press 4 to multiple two numbers")
selection = int(input(""))

if 1 <= selection <= 4:
    num1 = int(input("Please input the first number: "))
    num2 = int(input("Please input the second number: "))

    if selection == 1:
        print(str(num1 + num2))
    elif selection == 2:
        print(str(num1 - num2))
    elif selection == 3:
        print(str(num1 / num2))
    elif selection == 4:
        print(str(num1 * num2))
else:
    print("You did not make a valid selection.")
