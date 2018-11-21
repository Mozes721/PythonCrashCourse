def make_album(name, album):
    album_dict = {
        'artist': name,
        'album': album,
    }
    return album_dict

a = make_album('john', 'ace')
print(a)
b = make_album('Tom', 'YLY')
print(b)
c = make_album('Deadmouse', 47)
print(c)