#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-5 Movie Tickets

print("#7-5 Movie Tickets")
while True:
    age = input("Enter your age: ")
    age = int(age)
    if age <= 3:
        print("The ticket is free.")
        break
    if age > 3 and age <= 12:
        print("The ticket is $10.")
        break
    if age > 12:
        print("The ticket is $15.")
        break