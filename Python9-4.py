#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-4 Number Served

print("\n#9-4 Number Served")

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
	def describe_restaurant(self):
		print(self.restaurant_name.title(), "is a", self.cuisine_type.title(),
			"restaurant that has served", self.number_served, "customers.")
	def open_restaurant(self):
		print(self.restaurant_name.title(), "is now open for business.")
	def set_number_served(self, number_served):
		self.number_served = number_served
	def increment_number_served(self, served):
		self.number_served = self.number_served + served

restaurant = Restaurant('azteca', 'mexican')
print()
restaurant.describe_restaurant()
restaurant.number_served = 1000
restaurant.describe_restaurant()
restaurant.set_number_served(5000)
restaurant.describe_restaurant()
restaurant.increment_number_served(50)
restaurant.describe_restaurant()