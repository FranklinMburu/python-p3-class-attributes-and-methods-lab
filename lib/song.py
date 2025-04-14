class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

if __name__ == '__main__':
    # Example usage to test (you can remove this later)
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Run This Town", "Jay-Z", "Rap")
    song3 = Song("Halo", "Beyonce", "Pop")
    song4 = Song("Hotline Bling", "Drake", "Rap")
    song5 = Song("One Dance", "Drake", "Pop")

    print(f"Song Count: {Song.count}")
    print(f"Genres: {Song.genres}")
    print(f"Artists: {Song.artists}")
    print(f"Genre Count: {Song.genre_count}")
    print(f"Artist Count: {Song.artist_count}")