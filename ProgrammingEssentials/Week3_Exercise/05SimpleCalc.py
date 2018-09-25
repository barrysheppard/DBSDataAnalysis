# Question 5. Write the simple calc program which is given below with option
# 5 to exit. Write a program which displays a menu to the user. The menu
# should look similar to the following
# Welcome to the SimpleCalc
# Press 1 to add two numbers
# Press 2 to subtract two numbers
# Press 3 to divide two numbers
# Press 4 to multipy two numbers
# Read in the selection from the user and then ask the user for two numbers.
# Print the result to the user.
# Also ask the user if they want to continue or quit. (use loop)
# Using the simple calculator, ccreate functions to perform the following


def Add(x, y):
    """ Add which accepts two numbers """
    result = x + y
    return result


def Subtract(x, y):
    """ Subtract which accepts two numbers """
    result = x - y
    return result


def Divide(x, y):
    """Divide which accepts two numbers"""
    result = x / y
    return result


def Multiply(x, y):
    """ Mutiply which accepts to numbers """
    result = x + y
    return result

# We set selection to a valid value, to star the loop
# but will prompt the user for a new input at the start of the loop


selection = 1

while selection is not 5:
    print("Welcome to the SimpleCal")
    print("Press 1 to add two numbers")
    print("Press 2 to subtract two numbers")
    print("Press 3 to divide two numbers")
    print("Press 4 to multiply two numbers")
    print("Press 5 to Exit")
    selection = int(input("Your selection: "))

    if 1 <= selection <= 4:
        num1 = int(input("Please input the first number: "))
        num2 = int(input("Please input the second number: "))

        if selection == 1:
            print("The answer is: ", Add(num1, num2))
        elif selection == 2:
            print(Subtract(num1, num2))
        elif selection == 3:
            print(Divide(num1, num2))
        elif selection == 4:
            print(Multiply(num1, num2))
        elif selection == 5:
            print("Good Bye!")
    else:
        print("You did not make a valid selection.")
