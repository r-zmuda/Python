#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-10 Imported Restaurant

from restaurant import Restaurant
from restaurant import IceCreamStand

print("\n#9-10 Imported Restaurant")

restaurant = IceCreamStand('milky way', 'ice cream', 12000, 'chocolate',
	'vanilla', 'strawberry', 'pistachio', 'rocky road', 'blueberry',
	'cookie dough', 'orange sherbet')
print()
restaurant.describe_restaurant()
restaurant.show_flavors()