def make_album(art_name, alb_name, song_numb = "None"):
    """Creates a dictionary with artist name, album name and, optionally, song number."""
    albums = {
        'Art_name' : art_name,
        'Alb_name' : alb_name,
        }
    if song_numb:
        albums["song_numb"] = song_numb
    return albums

while True:
    print("\nPlease tell me about your favorite songs.")
    print("\nYou can enter 'q' to quit at any time.")
    art_nam = input("Artist's name: ")
    if art_nam == 'q':
        break
    alb_nam = input("Album's name: ")
    if alb_nam == 'q':
        break

album_1 = make_album(art_nam, alb_nam)
print(album_1)