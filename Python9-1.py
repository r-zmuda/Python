#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-1 Restaurant

print("\n#9-1 Restaurant")

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

restaurant = Restaurant('azteca', 'mexican')
print("\nrestaurant_name:", restaurant.restaurant_name)
print("cuisine_type:", restaurant.cuisine_type)
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()