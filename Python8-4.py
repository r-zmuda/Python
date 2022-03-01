#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-4 Large Shirts

print("\n#8-4 Large Shirts")
def make_shirt(shirt_size="large", shirt_message="i love python"):
    print('I will make a you a', shirt_size, 'T-Shirt with the message "' +
        shirt_message.title() + '".')
make_shirt()
make_shirt("medium")
make_shirt(shirt_message="best mom north america")
make_shirt(shirt_message="comic-con 2018", shirt_size="large")