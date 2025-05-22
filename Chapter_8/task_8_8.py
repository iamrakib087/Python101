def make_album(artist, title, number_of_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if number_of_songs is not None:
        album["number_of_songs"] = number_of_songs
    return album

print("Enter album information. Type 'quit' at any time to stop.")

while True:
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break


    songs_input = input("Number of songs (or press Enter to skip): ")
    if songs_input.lower() == 'quit':
        break

    if songs_input:
        album = make_album(artist, title, number_of_songs=int(songs_input))
    else:
        album = make_album(artist, title)

    print("Album created:", album)
    print()