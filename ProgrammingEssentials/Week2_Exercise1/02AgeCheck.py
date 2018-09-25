# Write a program that prompts the user to enter age. If age of the user is
# equals 18, then the proram displays "You are eligibel to vote". Otherwise
# the program displays "You cannot vote".

age = int(input("Please input your age: "))
if age == 18:
    print("You are eligibel to vote")
else:
    print("You cannot vote")

# I'm not sure why people older don't get to vote, but that was the spec
