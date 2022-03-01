#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-8 Deli

print("#7-8 Deli")
sandwich_orders = ['ham', 'turkey', 'bacon', 'cheese', 'roast beef']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Making " + sandwich.title() + " Sandwich...")
    finished_sandwiches.append(sandwich)
print("\nFinished making items:")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " Sandwich")