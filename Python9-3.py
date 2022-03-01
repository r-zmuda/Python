#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-3 Users

print("\n#9-3 Users")

class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print("\nUser Detail")
		print("First Name:", self.first_name.title())
		print("Last Name:", self.last_name.title())
	def greet_user(self):
		print("Greetings,", self.first_name.title(),
			self.last_name.title() + ".")

user1 = User('philip', 'jones')
user2 = User('julie', 'zhang')
user3 = User('robert', 'vincent')
user1.describe_user()
user2.describe_user()
user3.describe_user()
print()
user1.greet_user()
user2.greet_user()
user3.greet_user()