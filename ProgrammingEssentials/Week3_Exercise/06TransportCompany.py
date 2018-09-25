# Question 6. You have been asked to write a program for a local goods
# transport company. The company has the following pricing structure.
#
# Milage Rate 0-100 Miles €0.50 per mile. 101-200 Miles €0.40 per mile.
# 201+ Miles €0.30 per mile. Example 250 miles would cost €105 (50+40+15)
# Weight Rate 0-100 Kgs €0.33 per Kg. 101-200 Kgs €0.23 per Kg. 201+ Kgs €0.17
# per Kg. Example 250 Kgs would cost €64.50 (33+23+8.50)
# Regular Customer Discount. 7.5% off total bill.
#
# The program requires the clerk to enter the following information:
# How many miles must the item be transported?
# What is the weight of the items being transported?
# Is this a regular customer?
#
# The program should then displaythe Total amount for the bill. If a discount
# was applied show how much the value of the discount is. Write appropriate
# functions to calculate the each cost.


def MileageRate(miles):
    if miles >= 201:
        result = (miles-200)*0.3 + 90
    elif miles >= 101:
        result = (miles-100)*0.4 + 50
    else:
        result = miles * 0.5
    return result


def WeightRate(kgs):
    if kgs >= 201:
        result = (kgs-200)*0.17 + 56
    elif kgs >= 101:
        result = (kgs-100)*0.17 + 33
    else:
        result = kgs * 0.33
    return result


distance = int(input("How many miles must the item be transported? "))
weight = int(input("What is the weight of the items being transported? "))
regular = input("Is this a regular customer? Y/N ")

cost = MileageRate(distance) + WeightRate(weight)
if regular.lower() is "y":
    cost = cost * .925

print("The final charge is: ", cost)
