#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-5 Cities

print("\n#8-5 Cities")
def describe_city(city, country="america"):
    print(city.title(), "is in", country.title() + ".")
describe_city("new york city")
describe_city("seattle")
describe_city("vancouver", "canada")