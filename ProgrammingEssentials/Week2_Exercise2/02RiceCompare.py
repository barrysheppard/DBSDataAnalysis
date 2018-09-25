# Suppose you shop for rice in two different packages You would like to write
# a program to compare the cost. The program prompts the user to enter the
# weight and price of the each package and displays the one with the better
# price.

package1Weight = int(input("Please enter weight of package 1: "))
package1Price = int(input("Please enter price of package 1: "))
package2Weight = int(input("Please enter weight of package 2: "))
package2Price = int(input("Please enter price of package 2: "))

package1Value = package1Weight / package1Price
package2Value = package2Weight / package2Price

if package1Value > package2Value:
    print("You should buy package 1")
elif package2Value > package1Value:
    print("You should buy package 2")
else:
    print("You can get either package")
