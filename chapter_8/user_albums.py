def make_album(artist, title, track=0):
    album_dict = {
        'artists': artist.title(),
        'title': title.title(),
    }
    if track:
        album_dict['tracks'] = track
    return album_dict

title_promt= "\nWhat album are you thinking of?"
artists_promp = "Who's the artists?"

print("Enter 'quit' at any to stop.")

while True:
    titles = input(title_promt)
    if titles == 'quit':
        break

    artists = input(artists_promp)
    if artists == 'quit':
        break

    album = make_album(artists, titles)
    print(album)

print("\nThanks for responding!")



