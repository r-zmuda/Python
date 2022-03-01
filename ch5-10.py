# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-10 Checking Usernames

print("#5-10 Checking Usernames\n")

current_users = ['avarice', 'jello', 'jeckyll', 'chatbot', 'hyde']
new_users = ['Avarice', 'PeanuT', 'rhombus', 'JellO', 'pAndA']

for user in new_users:
    if user.lower() in current_users:
        print("Sorry, " + user.lower() + " is taken. Please choose " +
                "a different name.")
    else:
        print(user.lower() + " is available.")
