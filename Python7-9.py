#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-9 No Pastrami

print("#7-9 No Pastrami")
sandwich_orders = ['ham', 'pastrami', 'turkey', 'pastrami', 'bacon', 'cheese', 'pastrami', 'roast beef']
finished_sandwiches = []
print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Making " + sandwich.title() + " Sandwich...")
    finished_sandwiches.append(sandwich)
print("\nFinished making items:")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " Sandwich")