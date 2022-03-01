#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-16 Imports

#"import import_functions" caused error, isn't working
#"import import_functions as if" caused error, isn't working
from import_functions import make_car
car1 = make_car("honda", "civic", year=2010, color="gray")
from import_functions import build_profile as bp
profile1 = bp("ryan", "zmuda", age=30,
    occupation="student", field="software development")
from import_functions import *
album1 = make_album("rot", "end of the line", 7)
print("\n#8-16 Imports")
print("\n#car1")
print(car1)
print("\n#profile1")
print(profile1)
print("\n#sandwich")
make_sandwich("bacon", "salami")
print("\n#album1")
print(album1)