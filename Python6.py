#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 6

#6-1 Person
print("#6-1 Person\n")
person = {
    'first_name': 'samuel',
    'last_name': 'jackson',
    'age': 69,
    'city': 'los angeles'
    }
print("First Name:", person['first_name'].title())
print("Last Name:", person['last_name'].title())
print("Age:", person['age'])
print("City:", person['city'].title())
print()

#6-2 Favorite Numbers
print("#6-2 Favorite Numbers\n")
favNum = {'bobby': 7, 'samantha': 13, 'joel': 24, 'robert': 777, 'jessica': 47, 'shantae': 5}
for person, value in favNum.items():
    print(person.title() + ":", value)
print()

#6-3 Glossary
print("#6-3 Glossary\n")
glossary = {
    'concatenation': 'method of combining strings',
    'whitespace': 'nonprinting characters',
    'float': 'any number with a decimal point',
    'tuple': 'an immutable list',
    'dictionary': 'a collection of key-value pairs, like this one'
	}
for word, definition in glossary.items():
    print("- " + word.title() + ":\n ", definition + ".")
print()
	
#6-4 Glossary 2
print("#6-4 Glossary 2\n")
glossary = {
    'concatenation': 'method of combining strings',
    'whitespace': 'nonprinting characters',
    'float': 'any number with a decimal point',
    'tuple': 'an immutable list',
    'dictionary': 'a collection of key-value pairs, like this one'
	}
glossary['string'] = 'a series of characters'
glossary['method'] = 'an action performed on a piece of data'
glossary['index'] = 'the position of a value'
glossary['append'] = 'a method that adds a new element to a list'
glossary['slice'] = 'a specific group of items in a list'
for word, definition in glossary.items():
    print("- " + word.title() + ":\n ", definition + ".")
print()

#6-5 Rivers
print("#6-5 Rivers\n")
rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'rio grande': 'mexico',
    'mississippi river': 'the united states',
    'rhine': 'germany'
    }
for river, country in rivers.items():
    print("The", river.title(), "runs through", country.title() + ".")
print()
print("Rivers:")
for river in rivers.keys():
    print("* " + river.title())
print()
print("Countries:")
for country in rivers.values():
    print("* " + country.title())
print()

#6-6 Polling
print("#6-6 Polling\n")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
take_poll = ['samuel', 'jen', 'bobby', 'phil', 'george', 'regina']
for name in take_poll:
    if not name in favorite_languages.keys():
        print(name.title() + ", please take our poll!")
    else:
        print(name.title() + ", thank you for taking the poll.")
print()

#6-7 People
print("#6-7 People\n")
person1 = {'first_name': 'samuel', 'last_name': 'jackson', 'age': 69, 'city': 'los angeles'}
person2 = {'first_name': 'hugh', 'last_name': 'jackman', 'age': 49, 'city': 'melbourne'}
person3 = {'first_name': 'kaenu', 'last_name': 'reeves', 'age': 53, 'city': 'manhattan'}
people = [person1, person2, person3]
for person in people:
    print("First Name:", person['first_name'].title())
    print("Last Name:", person['last_name'].title())
    print("Age:", person['age'])
    print("City:", person['city'].title())
    print()

#6-8 Pets
print("#6-8 Pets")
king = {'name': 'king', 'species': 'dog', 'breed': 'german shepherd', 'owner': 'antonio'}
luna = {'name': 'luna', 'species': 'dog', 'breed': 'siberian husky', 'owner': 'gina'}
daisy = {'name': 'daisy', 'species': 'dog', 'breed': 'golden retriever', 'owner': 'connie'}
homer = {'name': 'homer', 'species': 'dog', 'breed': 'beagle', 'owner': 'paul'}
pets = [king, luna, daisy, homer]
for pet in pets:
    print(pet['owner'].title() + "'s " + pet['species'] + " " + pet['name'].title() + " is a " + pet['breed'].title() + ".")
print()

#6-9 Favorite Places
print("#6-9 Favorite Places\n")
favorite_places = {
    'tyson': ['australia', 'germany', 'brazil'],
    'brittany': ['france', 'russia', 'egypt'],
    'jason': ['switzerland', 'japan', 'spain'],
    }
for person, places in favorite_places.items():
    print(person.title() + "'s favorite places are:")
    for place in places:
        print("* " + place.title())
print()

#6-10 Favorite Numbers
print("#6-10 Favorite Numbers\n")
favNum = {
    'bobby': [7, 12, 3],
    'samantha': [33, 13, 3, 300],
    'joel': [24, 2],
    'robert': [777, 666, 0],
    'jessica': [21, 47, 1987],
    'shantae': [1, 5]
    }
for person, numbers in favNum.items():
    print(person.title() + "'s favorite numbers:")
    for number in numbers:
        print("* " + str(number))
print()

#6-11 Cities
print("#6-11 Cities\n")
cities = {
    'new york city': {
        'country': 'united states',
        'population': '8.538 million',
        'fact': 'The Empire State Building in New York City stands at 1250 ft.'
        },
    'orlando': {
        'country': 'united states',
        'population': '277,173',
        'fact': 'Orlando is home of Walt Disney World.'
        },
    'seattle': {
        'country': 'united states',
        'population': '704,352',
        'fact': 'Seattle has a thriving tech industry.'
        },
    }
for key, city in cities.items():
    print(key.title())
    for key, value in city.items():
        print("* " + key.title() + ": " + value)
print()

#6-12 Extensions
print("#6-12 Extensions\n")
king = {'id': '0187', 'name': 'king', 'species': 'dog', 'breed': 'german shepherd', 'owner': 'antonio lopez'}
luna = {'id': '1073', 'name': 'luna', 'species': 'dog', 'breed': 'siberian husky', 'owner': 'gina johanneson'}
daisy = {'id': '2697', 'name': 'daisy', 'species': 'dog', 'breed': 'golden retriever', 'owner': 'connie williams'}
homer = {'id': '9162', 'name': 'homer', 'species': 'dog', 'breed': 'beagle', 'owner': 'paul renolds'}
peach = {'id': '0727', 'name': 'peach', 'species': 'dog', 'breed': 'rottweiler', 'owner': 'amanda phelps'}
palpatine = {'id': '3173', 'name': 'palpatine', 'species': 'cat', 'breed': 'himalayan cat', 'owner': 'jorge gutierrez'}
rex = {'id': '1243', 'name': 'rex', 'species': 'cat', 'breed': 'nebelung', 'owner': 'michael applegate'}
sydney = {'id': '5617', 'name': 'sydney', 'species': 'cat', 'breed': 'siamese cat', 'owner': 'maxwell baldwin'}
candy = {'id': '2967', 'name': 'candy', 'species': 'hamster', 'breed': 'chinese hamster', 'owner': 'courtney tran'}
pets = [king, luna, daisy, homer, peach, palpatine, rex, sydney, candy]
i = 1
print("Pet Database")
print("Searching for pet data...")
for pet in pets:
    print("\nPet Data# " + pet['id'])
    for data, value in pet.items():
        print("* " + data.title() + ": " + value.title())
    i = i + 1
print("\nReturned " + str(i) + " entries.")
