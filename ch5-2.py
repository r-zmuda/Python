# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-2 More Conditional Tests

print("#5-2 More Conditional Tests\n")

# Variables
string1 = "apple"
string2 = "Penguin"
num1 = 7
num2 = 13
num3 = 18
num4 = 21
sports = ['basketball', 'soccer', 'football', 'baseball']

# Show values
print("string1: " + string1)
print("string2: " + string2)
print("num1: " + str(num1))
print("num2: " + str(num2))
print("num3: " + str(num3))
print("num4: " + str(num4))
print("sports: " + str(sports))

# Test 11
print("\n11. Is string1 not equal to 'apple'?")
print(string1 != 'apple')

# Test 12
print("\n12. Is string2 equal to 'penguin' (using .lower())?")
print(string2.lower() == 'penguin')

# Test 13
print("\n13. Is num1 equal to num2?")
print(num1 == num2)

# Test 14
print("\n14. Is num3 not equal to num4?")
print(num3 != num4)

# Test 15
print("\n15. Is num1 greater than num3?")
print(num1 > num3)

# Test 16
print("\n16. Is num2 less than num4?")
print(num2 < num4)

# Test 17
print("\n17. Is num4 greater than or equal to num1?")
print(num1 >= num4)

# Test 18
print("\n18. Is num2 less than or equal to num3?")
print(num2 <= num3)

# Test 19
print("\n19. Is num2 greater than num1 and less than num3?")
print(num2 > num1 and num2 < num3)

# Test 20
print("\n20. Is num3 less than num2 or greater than num1?")
print(num3 < num2 or num3 > num1)

# Test 21
print("\n21. Does sports contain 'bowling'?")
if 'bowling' in sports:
    print("True")
else:
    print("False")
    
# Test 22
print("\n22. Does sports not contain 'golf'?")
if 'golf' not in sports:
    print("True")
else:
    print("False")
