from song import Song
from album import Album


class Band:
	def __init__(self, name):
		self.name = name
		self.albums = []

	def add_album(self, album):
		if album not in self.albums:
			self.albums.append(album)
			return f"Band {self.name} has added their newest album {album.name}."

		return f"Band {self.name} already has {album_name.name} in their library."

	def remove_album(self, album_name):
		for album in self.albums:
			if album.name == album_name:
				if album.published:
					return f"Album has been published. It cannot be removed."
				self.albums.remove(album)
				return f"Album {album.name} has been removed."
		return f"Album {album_name} is not found."

	def details(self):
		new_list = [f'{a.details()}\n' for a in self.albums]
		new_string = ''.join(new_list)
		return f'Band {self.name}\n{new_string}'



song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())