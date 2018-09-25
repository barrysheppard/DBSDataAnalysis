# Create a console application which will ask the user to enter a number
# between 0 and 1000. The program will then determine if the number entered
# is an even number or not. If the number enetered is an even number show the
# message "The number you entered is even". If the number entered is odd show
# the message "The number you entered is odd". If the user enters an invalid
# number show the message "You entered an invalid number". In this case an
# invalid number is less than 1 or greater than 1000.

userNumber = int(input("Enter a number between 1 and 1000: "))
if 1 <= userNumber <= 1000:
    if (userNumber % 2) == 0:
        print("The number you entered is even")
    else:
        print("The number you entered is odd")
else:
    print("You entered an invalid number")
