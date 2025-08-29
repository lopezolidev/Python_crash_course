def make_album(artist_name, album_title, number_of_songs=None):
    album = { 'artist': artist_name,
             'title': album_title}
    
    if number_of_songs:
        album['songs'] = number_of_songs

    return album

while True:
    print("\nPlease, give me the name of the artist, album title and (optional: " \
    "number of songs)")
    print("(Enter 'q' to end the program)")

    name = input("Artist name: ")
    
    if name == 'q':
        break

    title = input("Album title: ")

    number = input("(optional) Number of songs: ")
    if number == '':
        number = None
    
    print(make_album(name, title, number))