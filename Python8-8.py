#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-8 User Albums

print("\n#8-8 User Albums")
#Variables
albums = []
temp_album = {}
make_albums = True
got_num = False
#Functions
def make_album(artist, title, tracks=1):
    album = {'artist_name': artist, 'album_title': title,
        'album_tracks': tracks}
    return album
#Start program
print("Enter 'q' at any time to exit.")
while make_albums:
    #Get input, q to quit
    temp_artist = input("\nEnter album artist: ")
    if temp_artist == 'q':
        break
    temp_title = input("Enter album title: ")
    if temp_title == 'q':
        break
    temp_tracks = input("Enter number of tracks on album: ")
    if temp_tracks == 'q':
        break
    while not got_num:
        try:
            temp_tracks = int(temp_tracks)
            got_num = True
        except ValueError:
            print("Error: Invalid input. Not a number.")
            temp_tracks = input("Enter number of tracks on album: ")
    #Make album, output list
    temp_album = make_album(temp_artist, temp_title, temp_tracks)
    albums.append(temp_album)
    print("Album added.")
    print("\nCurrent list of albums:")
    for album in albums:
        print(album)
    got_num = False
print("Program finished.")