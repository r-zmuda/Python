#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-4 Pizza Toppings

print("#7-4 Pizza Toppings")
pizza = []
print("Let's build a pizza.")
while True:
    topping = input("Request topping or type 'order': ")
    if topping == 'order':
        break
    else:
        pizza.append(topping)
for toppings in pizza:
    print("Adding " + toppings + "...")
print("Your pizza is ready.")