#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-12 Multiple Modules

from user import User

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