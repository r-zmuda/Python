# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-9 No Users

print("#5-9 No Users\n")

users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see " +
                    "a status report?")
        else:
            print("Welcome back, " + user + ".")
else:
    print("We need to find some users!")
