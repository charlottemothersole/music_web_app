class Artist():
    def __init__(self, id, artist, genre):
        self.id = id
        self.artist = artist
        self.genre = genre
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.artist}, {self.genre})"