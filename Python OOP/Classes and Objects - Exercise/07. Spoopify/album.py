class Album:
	def __init__(self, name, *args):
		self.name = name
		self.song = list(args)
		self.published = False

	def add_song(self, song):
		if self.published:
			return f'Cannot add songs. Album is published.'
		if song in self.song:
			return f'Song is already in the album.'
		if song.single:
			return f"Cannot add {song.name}. It's a single"

		self.song.append(song)
		return f'Song {song.name} has been added to the album {self.name}.'

	def remove_song(self, song_name):
		if self.published:
			return f'Cannot remove songs. Album is published.'
		filtered_songs = [s for s in self.song if s.name == song_name]
		if not filtered_songs:
			return f'Song is not in the album.'
		song = filtered_songs[0]
		self.song.remove(song)
		return f'Removed song {song_name} from album {self.name}.'

	def publish(self):
		if self.published:
			return f'Album {self.name} is already published.'

		self.published = True
		return f'Album {self.name} has been published.'

	def details(self):
		new_list = [f'== {s.get_info()}\n' for s in self.song]
		new_string = ''.join(new_list)
		return f'Album {self.name}\n{new_string}'