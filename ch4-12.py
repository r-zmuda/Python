#Ryan Zmuda
#SOFT 204 Open Source Programming
#4-12 More Loops

print("#4-12 More Loops\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
f_foods = my_foods[:]

my_foods.append('cannoli')
f_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy friend's favorite foods are:")
for food in f_foods:
    print(food.title())
