#Ryan Zmuda
#SOFT 204 Open Source Programming
#4-10 Slices

print("#4-10 Slices\n")

pizzas = ['pepperoni', 'bacon', 'mushroom', 'jalapeno', 'ham', 'pineapple', 'steak', 'cheese', 'sausage']
print("The first three pizzas in the list are:")
for pizza in pizzas[:3]:
    print(pizza.title())
print("\nThree of the middle pizzas in the list are:")
for pizza in pizzas[3:6]:
    print(pizza.title())
print("\nThe last three pizzas in the list are:")
for pizza in pizzas[-3:]:
    print(pizza.title())
