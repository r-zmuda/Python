#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-11 Unchanged Magicians

print("\n#8-11 Unchanged Magicians")
magicians = ['trixie', 'summer', 'houdini', 'christopher']
great_magicians = []
def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())
def make_great(list_of_magicians):
    list_of_great_magicians = []
    index = 0
    while index < len(list_of_magicians):
        list_of_great_magicians.append(list_of_magicians[index] +
            " the Great")
        index += 1
    return list_of_great_magicians
great_magicians = make_great(magicians)
print("#List of Magicians:")
show_magicians(magicians)
print("#List of Great Magicians:")
show_magicians(great_magicians)