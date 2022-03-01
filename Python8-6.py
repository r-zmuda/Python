#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-6 City Names

print("\n#8-6 City Names")
def city_country(city, country):
    return city.title() + ", " + country.title()
city1 = city_country("paris", "france")
city2 = city_country("warsaw", "poland")
print(city_country("frankfurt", "germany"))
print(city1)
print(city2)