#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-12 Sandwiches

print("\n#8-12 Sandwiches")
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient.title())
make_sandwich("pork")
make_sandwich("bacon", "ham", "mayonaise")
make_sandwich("beef", "tomato", "salami", "mustard")