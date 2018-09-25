# Question 4. Write a program that aks the user to enter the age of 10
# post-grd strudents and stores the age in a list. Write a function that
# calculates the average of all ages in the List. Invoke this function and
# print the results.

studentAgeList = [] # This makes an empty list

studentAge = input("Enter Student Age or EXIT to Quit :")
while studentAge.lower() != "exit":
    studentAgeList.append(int(studentAge))
    studentAge = input("Enter Student Age or EXIT to Quit :")

def AverageAge(ages):
    count = len(ages)
    total = sum(ages)
    result = total/count
    return result

result = AverageAge(studentAgeList)
print("Average age is :", result)
