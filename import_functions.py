def make_car(manufacturer, model, **features):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in features.items():
        car[key] = value
    return car

def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient.title())

def make_album(artist, title, tracks=1):
    album = {'artist_name': artist, 'album_title': title, 'album_tracks': tracks}
    return album