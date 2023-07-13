from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection
        pass

    def all(self):
        rows = self._connection.execute('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = Artist(row['id'], row['artist'], row['genre'])
            artists.append(item)
        return artists

    def create(self, artist):
        self._connection.execute(
            'INSERT INTO artists (artist, genre) VALUES (%s, %s)',
            [artist.artist, artist.genre]
        )
        return None