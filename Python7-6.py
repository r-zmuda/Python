#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-6 Three Exits

print("#7-6 Three Exits")
total = 0
active = True
while active:
    x = 0
    people = input("How many people are in your group?: ")
    people = int(people)
    while x < people:
        x += 1
        age = input("Enter age for person #" + str(x) + ": ")
        age = int(age)
        if age <= 3:
            print("The ticket is free.")
        if age > 3 and age <= 12:
            print("The ticket is $10.")
            total += 10
        if age > 12:
            print("The ticket is $15.")
            total += 15
    print("Your total is $" + str(total) + ".")
    print("Enjoy the show.")
    while True:
        answer = input("Process another group (yes or no)?: ")
        if answer == 'yes':
            break
        if answer == 'no':
            active = False
            break
        else:
            print("Type 'yes' or 'no'.")