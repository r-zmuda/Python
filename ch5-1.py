# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-1 Conditional Tests

print("#5-1 Conditional Tests\n")

# Variables
my_number = 30
my_boolean = True
my_string = "rectangle"
my_list = ['red', 'yellow', 'green']
my_tuple = ('purple', 'blue', 'white')

# Show values
print("my_number: " + str(my_number))
print("my_boolean: " + str(my_boolean))
print("my_string: " + my_string)
print("my_list: " + str(my_list))
print("my_tuple: " + str(my_tuple))

# Test 1
print("\n1. Is my_number greater than 20?")
print(my_number > 20)

# Test 2
print("\n2. Is my_number less than or equal to 27?")
print(my_number <= 27)

# Test 3
print("\n3. Is my_boolean equal to False?")
print(my_boolean == False)

# Test 4
print("\n4. Is my_boolean equal to True?")
print(my_boolean == True)

# Test 5
print("\n5. Is my_string equal to 'triangle'?")
print(my_string == 'triangle')

# Test 6
print("\n6. Is my_string equal to 'rectangle'?")
print(my_string == 'rectangle')

# Test 7
print("\n7. Does my_list contain 'red'?")
if 'red' in my_list:
    print("True")
else:
    print("False")

# Test 8
print("\n8. Does my_list contain 'purple'?")
if 'purple' in my_list:
    print("True")
else:
    print("False")

# Test 9
print("\n9. Does my_tuple contain 'black'?")
if 'black' in my_tuple:
    print("True")
else:
    print("False")

# Test 10
print("\n10. Does my_tuple contain 'white'?")
if 'white' in my_tuple:
    print("True")
else:
    print("False")
