#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-11 Imported Admin

from admin import User
from admin import Admin
from admin import Privileges

print("\n#9-11 Imported Admin")

user1 = Admin('ariana', 'grande', 9)
user1.describe_user()
user1.privileges.show_privileges()