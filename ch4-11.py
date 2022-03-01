#Ryan Zmuda
#SOFT 204 Open Source Programming
#4-11 My Pizzas, Your Pizzas

print("#4-11 My Pizzas, Your Pizzas\n")

my_pizzas = ['pepperoni', 'bacon', 'mushroom', 'jalapeno', 'ham', 'pineapple']
f_pizzas = my_pizzas[:]

my_pizzas.append('steak')
f_pizzas.append('sausage')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in f_pizzas:
    print(pizza.title())
