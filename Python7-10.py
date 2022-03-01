#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-10 Dream Vacation

print("#7-10 Dream Vacation")
answers = {}
polling = True
while polling:
    name = input("What's your name? ")
    answer = input("If you could visit one place in the world, where would you go? ")
    answers[name] = answer
    another = input("Would you like to let another person respond? (yes/no): ")
    if another == 'no':
        polling = False
print("\nPoll results:")
for name, answer in answers.items():
    print(name.title() + " would like to visit " + answer.title() + ".")