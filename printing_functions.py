#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-15 Printing Models - Printing Functions

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design.title())
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())