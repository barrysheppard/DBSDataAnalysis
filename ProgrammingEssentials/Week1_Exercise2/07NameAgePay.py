# Week 1 Exercise 2
# Exercise 7: Write a program that prompts the user to enter name, age, gross
# pay and tax rate. The program then calculates the net pay and displays the
# user name, age, gross pay, tax rate, and net pay on the console.

name = input("Enter your name: ")
age = input("Enter your age: ")
grosspay = input("Enter your gross pay: ")
taxrate = input("Enter your tax rate: ")

netpay = float(grosspay) - float(grosspay) * float(taxrate) * .01

print("Your name is :" + name)
print("Your age is :" + age)
print("Your gross pay is: " + grosspay)
print("Your tax rate in % is: " + taxrate)
print("Your net pay is: " + str(netpay))
