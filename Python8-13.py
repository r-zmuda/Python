#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-13 User Profile

print("\n#8-13 User Profile")
def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("ryan", "zmuda", age=30, occupation="student",
    location="united states", field="software development")
print (user_profile)