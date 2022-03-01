#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#7-2 Restaurant Seating

print("#7-2 Restaurant Seating")
party = input("How many people?: ")
party = int(party)
if party > 8:
    print("You will have to wait to be seated.")
else:
    print("Party of " + str(party) + ", be seated.")