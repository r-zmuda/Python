#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-12 Multiple Modules

from admin2 import Admin
from admin2 import Privileges

print("\n#9-12 Multiple Modules")

user1 = Admin('julie', 'winters', 7)
user1.describe_user()
user1.privileges.show_privileges()