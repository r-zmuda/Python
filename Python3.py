#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 3

#List of Functions (16)
#title(): Returns string in titlecase
#print(): Displays string value
#upper(): Returns string in uppercase
#lower(): Returns string in lowercase
#rstrip(): Trims end of a string of whitespace
#lstrip(): Trims beginning of a string of whitespace
#strip(): Trims both sides of a string of whitespace
#str(): Represent non-string value as string
#append(): Adds value to a list
#insert(): Inserts value to a list at index
#pop(): Removes last value from a list, returns value
#remove(): Removes first instance of value from a list
#sort(): Changes the order of a list from original to alphabetical order
#sorted(): Returns ordered list without affecting original list
#reverse(): Reverses the order of a list
#len(): Returns length of a list

#3-3 Your Own List
print("#3-3 Your Own List")
cars = ['honda', 'toyota', 'subaru', 'mitsubishi', 'ford', 'audi','volkswagen', 'bmw', 'jaguar', 'porshe']
for car in cars:
	print(car.title())
print

#3-4 Guest List
print("#3-4 Guest List")
guests = ['katie', 'ron', 'jessica']
for guest in guests:
	print(guest.title() + ", I would like to invite you to dinner.")
print("Unfortunately, " + guests[1].title() + " can't make it to dinner.")
print

#3-5 Changing Guest List
print("#3-5 Changing Guest List")
guests.pop(1)
guests.append("samantha")
for guest in guests:
	print(guest.title() + ", I would like to invite you to dinner.")
print("I have ordered a large table to prepare.")
print("There is room for additional guests.")
print

#3-6 More Guests
print("#3-6 More Guests")
guests.insert(0, "charlotte")
guests.insert(int(len(guests)/2), "jonathan")
guests.append("christian")
for guest in guests:
	print(guest.title() + ", I would like to invite you to dinner.")
print("Disaster! My dog broke the dinner table.")
print("To make matters worse, the order for the large table has been delayed.")
print("I'll have to bust out the smaller, older dinner table from the garage.")
print("I can only have two guests at this table.")
print

#3-7 Shrinking Guest List
print("#3-7 Shrinking Guest List")
while len(guests) > 2:
	print("Sorry, " + guests.pop().title() + ", I can no longer have you to dinner.")
for guest in guests:
	print(guest.title() + ", you are still invited to dinner.")
totalGuests = len(guests) #Used for 3-10
while len(guests) > 0:
	del guests[0]
print(guests)
print

#3-8 Seeing the World
print("#3-8 Seeing the World")
print("* Locations Initial:")
locations = ['japan', 'germany', 'netherlands', 'sweden', 'australia']
print(locations)
print("* Locations Sorted:")
print(sorted(locations))
print("* Locations Original:")
print(locations)
print("* Locations Reversed:")
locations.reverse()
print(locations)
print("* Locations Redux:")
locations.reverse()
print(locations)
print("* Locations Sort:")
locations.sort()
print(locations)
print("* Locations Sort Reverse:")
locations.sort(reverse=True)
print(locations)
print

#3-9 Dinner Guests
print("#3-9 Dinner Guests")
print("I am having " + str(totalGuests) + " people over for dinner.")
print

#3-10 Every Function
print("#3-10 Every Function")
companies = ['microsoft', 'uber', 'amazon', 'google', 'apple', 'costco', 'valve']
print("* I've created a list of companies, such as " + companies[3].title() + ".")
print(companies)
print("* I decided to remove " + companies[1].title() + " from the list.")
companies.pop(1)
print(companies)
print("* I changed my mind. I'm putting it back in.")
companies.append("uber")
print(companies)
print("* I want to insert a company to the list.")
companies.insert(2, "f5")
print(companies)
print("* The list now contains " + str(len(companies)) + " companies.")
print("* I think it looks better reversed.")
companies.reverse()
print(companies)
print("* No way, the original order was better.")
companies.reverse()
print(companies)
print("* This list is a mess. What would it look like sorted?")
print(sorted(companies))
print("* Okay, let's sort it alphabetically.")
companies.sort()
print(companies)
print("* What about reverse alphabetical order?")
companies.sort(reverse=True)
print(companies)
