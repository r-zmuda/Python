print("\n#Ryan Zmuda")
print("#SOFT 204 Open Source Programming")
print("#Python Quiz")

print("\n#Complete the script so that it prints out the second letter of the list.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

print("\n#Complete the script so that it prints out a list containing letters d, e, f.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])

print("\n#Complete the script so that it prints out a list containing the first three elements of list letters.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])

print("\n#Complete the script so that it prints out the letter i using negative indexing.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2:-1])

print("\n#Complete the script so that it prints out a list containing the last three elements of list letters.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

print("\n#Complete the script so that it prints out a list containing letters a, c, e, g, and i so the at a step of two.")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
index = 0
while index < len(letters):
    if index % 2 == 0:
        print(letters[index])
    index += 1

print("\n#Create a script that generates a list of numbers from 1 to 20. Do not create a list manually.")
items = []
numbers = 20 #Numbers to generate
item = 1 #Count from 1
index = 0
while item <= numbers:
    items.append(item)
    item += 1
while index < len(items):
    print(items[index])
    index += 1

print("\n#Create a script that generates the list created above whose items are products of the original list items multiplied by 10.")
products = []
index = 0
while index < len(items):
    products.append(items[index] * 10)
    index += 1
index = 0
while index < len(products):
    print(products[index])
    index += 1

print("\n#Create and print a dictionary of two keys, a and b and two values 1 and 2 for keys a and b respectively.")
dictionary = {'a': 1, 'b': 2}
index = 0
for k, v in dictionary.items():
    print(k, v)

print("\n#Using the dictionary created above, print out the value of key b.")
print(dictionary['b'])

print("\n#Using the same dictionary, calculate the sum of value of key a and value of key b and print it out.")
sum = 0
for k, v in dictionary.items():
    sum += v
print(sum)

print("\n#Add a c key with a value of 3 to your dictionary and print out the updated dictionary.")
dictionary['c'] = 3
for k, v in dictionary.items():
    print(k, v)

print("\n#Find the sum of all values of your dictionary and print to screen.")
sum = 0
for k, v in dictionary.items():
    sum += v
print(sum)

print("\n#Create a new dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out.")
dictionary = {'a': [], 'b': [], 'c': []}
item = 1 #Count from 1
index = 0
for k, v in dictionary.items():
    while index < 10:
        v.append(item)
        item += 1
        index += 1
    index = 0
for k, v in dictionary.items():
    print(k, v)

print("\n#Access the third value of key b.")
print(dictionary['b'][2])