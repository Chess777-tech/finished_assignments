import random

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"{song} has been added to {self.name}.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} has been removed from {self.name}.")
        else:
            print(f"{song} is not in {self.name}.")

    def shuffle(self):
        random.shuffle(self.songs)
        print(f"{self.name} has been shuffled.")

    def play(self):
        if not self.songs:
            print(f"{self.name} is empty.")
        else:
            print(f"Now playing {self.name}:")
            for song in self.songs:
                print(song)

# Example usage:
my_playlist = Playlist("My Playlist")
my_playlist.add_song("Song 1") # Song 1 has been added to My Playlist.
my_playlist.add_song("Song 2") # Song 2 has been added to My Playlist.
my_playlist.add_song("Song 3") # Song 3 has been added to My Playlist.
my_playlist.play() # Now playing My Playlist:\nSong 1\nSong 2\nSong 3
my_playlist.remove_song("Song 2") # Song 2 has been removed from My Playlist.
my_playlist.shuffle() # My Playlist has been shuffled.
my_playlist.play() # Now playing My Playlist:\nSong 1\nSong 3
