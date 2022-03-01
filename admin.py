#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-11 Imported Admin

class User():
	def __init__(self, first_name, last_name, login_attempts=0):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts
	def describe_user(self):
		print("\nUser Detail")
		print("First Name:", self.first_name.title())
		print("Last Name:", self.last_name.title())
		print("Login Attempts:", self.login_attempts)
	def greet_user(self):
		print("Greetings,", self.first_name.title(),
			self.last_name.title() + ".")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	def __init__(self, first_name, last_name, login_attempts=0):
		super().__init__(first_name, last_name, login_attempts)
		self.privileges = Privileges('Can add posts', 'Can delete posts',
			'Can ban users')

class Privileges():
	def __init__(self, *privileges):
		self.privileges = privileges
	def show_privileges(self):
		print("\nAccount Privileges:")
		for priv in self.privileges:
			print("*", priv)