# Write a program that reads three edges a, b, and c, for a triangle and
# computes the perimeter if the input is valid. Otherwise, display that the
# input is invalid. The input is valid if the sum of every pair of two edges
# is greater than the remaining edge (perimeter = a+b+c).

edgeA = int(input("Enter the length of the first triangle edge: "))
edgeB = int(input("Enter the length of the second triangle edge: "))
edgeC = int(input("Enter the length of the third triangle edge: "))

if edgeA + edgeB > edgeC and edgeA + edgeC > edgeB and edgeC + edgeB > edgeA:
    print("The perimeter of the triangle is:", edgeA + edgeB + edgeC)
else:
    print("The edge values are not valid for a triangle")
