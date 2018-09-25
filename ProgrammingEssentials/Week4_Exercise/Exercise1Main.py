# Week 4 Exercise 1 - Continued from Exercise1Classes.py
# Create a variable named myTriangle and set it equal to a new instance of
# your triangle class. Pass it three angles that sum to 180, e.g 90, 30, 60.

from Exercise1Classes import Triangle

myTriangle = Triangle(90, 30, 60)

# Print out the number of sides using the Public Property (getter) and print
# out myTriangle.CheckAngles()

print(myTriangle.NumberOfSides())
print(myTriangle.CheckAngles())
