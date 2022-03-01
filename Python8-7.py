#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-7 Album

print("\n#8-7 Album")
def make_album(artist, title, tracks=1):
    album = {'artist_name': artist.title(), 'album_title': title.title(),
        'album_tracks': tracks}
    return album
album1 = make_album("the kronk", "new groove")
album2 = make_album("lunatic high", "limit break", 13)
album3 = make_album("paradox", "musician as outsider", 10)
print("#List of Albums:")
print(album1)
print(album2)
print(album3)