class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):

        for album in self.albums:
            if album_name == album.name:
                if album.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album.name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        res = '\n'.join(a.details() for a in self.albums)
        return f"Band {self.name}\n" \
               f"{res}"
