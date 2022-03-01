#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-2 Three Restaurants

print("\n#9-2 Three Restaurants")

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title(), "is a",
			self.cuisine_type.title(), "restaurant.")
	def open_restaurant(self):
		print(self.restaurant_name.title(),
			"is now open for business.")

restaurant1 = Restaurant('azteca', 'mexican')
restaurant2 = Restaurant('panda express', 'chinese')
restaurant3 = Restaurant('casa mia', 'italian')
print()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()