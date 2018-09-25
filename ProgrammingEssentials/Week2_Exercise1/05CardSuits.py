# Write a program that prompts the user for either 1, 2, 3 or 4.
# In your python code you will need to print out what 1, 2, 3 and 4 correspond
# to using below:
# 1=diamond, 2=hearts, 3=clubs and 4 - spades respectively.

suits = {1: "diamond", 2: "hearts", 3: "clubs", 4: "spades"}
userNumber = int(input("Pick a number between 1 and 4: "))
if 1 >= userNumber >= 4:
    print(suits[userNumber])
else:
    print("That number is not between 1 and 4!")
