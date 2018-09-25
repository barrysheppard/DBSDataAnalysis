# The Young and Beautiful Travel Company restricts its clients to ages between
# 18 and 30. Write a program to input a client's age and test whether they are
# eligible to go on vacation with the company or not.

age = int(input("Input the client's age: "))
if 18 <= age <= 30:
    print("The client is eligible to go on vacation.")
else:
    print("The client is not eligible to go on vacation.")
