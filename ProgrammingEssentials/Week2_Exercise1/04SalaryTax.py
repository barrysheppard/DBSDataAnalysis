# Write a program to input a salary from the user and determine how much tax
# someone should pay according to the following rules:
# People pay no tax if they earn up to €10,000
# They pay tax at the rate of 20% on the amount they earn over €10,000 but up
# to €50,000.
# They pay tax at 40% on any money they earn over €50,000

salary = int(input("Enter you salary in Euro: "))
if salary > 50000:
    tax = (salary-50000)*0.4 + (salary-10000)*0.2
elif salary > 10000:
    tax = (salary-10000)*0.2
else:
    tax = 0

# Converting to an int to remove decimals
tax = int(tax)
print("You should pay €", tax, "in tax.")
