#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-10 Great Magicians

print("\n#8-10 Great Magicians")
magicians = ['trixie', 'summer', 'houdini', 'christopher']
def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())
def make_great(list_of_magicians):
    index = 0
    while index < len(list_of_magicians):
        list_of_magicians[index] = list_of_magicians[index] + " the Great"
        index += 1
make_great(magicians)
print("#List of Great Magicians:")
show_magicians(magicians)