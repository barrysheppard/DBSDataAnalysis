# Homework
input_number = input("Please enter a number to factor: ")
factorial_result = 1
for i in range(1, int(input_number)+1):
    factorial_result = factorial_result * i

# Using this format, %s indicates a string, $d indicates a decimal
print("The factorial of %s is %d" % (input_number, factorial_result))
