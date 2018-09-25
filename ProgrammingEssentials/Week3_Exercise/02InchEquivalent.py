# Question 2. Write a function which returns the inch equivalent of its
# centimere argument. An example call is inches = InchEquivalent(10.5)
# mutliple centimeters by 0.394 to calculate inches.

def InchEquivalent(centimeters):
    inches = centimeters * 0.394
    return inches

print(InchEquivalent(10.5))
