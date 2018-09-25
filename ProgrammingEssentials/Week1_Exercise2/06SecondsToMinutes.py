# Week 1 Exercise 2
# Exercise 6: Write a program to prompt the user to enter time in seconds.
# The program then displays it in minutes and seconds.

totalseconds = input("Enter a time in seconds: ")

# Floor division will give the number of minutes
minutes = int(totalseconds)//60
# Modulus division will give us the remainder in seconds
seconds = int(totalseconds) % 60
# Print the result
print("There are " + str(minutes) + " Minutes: " + str(seconds) + " Seconds")
