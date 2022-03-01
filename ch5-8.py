# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-8 Hello Admin

print("#5-8 Hello Admin\n")

users = ['avarice', 'jello', 'jeckyll', 'admin', 'chatbot', 'hyde']

for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see " +
                "a status report?")
    else:
        print("Welcome back, " + user + ".")
