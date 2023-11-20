#The function should take an artist name and an album title
# and return a dictionary containing these two pieces of information
def make_album(artist_name, album_title, number_of_songs= "None"):
    """Makes a dictionary describing a music album"""
    album = {'artist': artist_name, 'album_title' : album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

musician = make_album ("name_1", "album_1", "13")
print(musician)
musician = make_album ("name_2", "album_2")
print(musician)
musician = make_album ("name_3", "album_3", "10")
print(musician)