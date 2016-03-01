import webbrowser


#class Movie
class Movie():
	"""This class provides a way to store movie related information

	Attributes:
		VALID_RATINGS (str array): array of valid censorship ratings

	Args:
        title (str): Title.
        storyline (str): Plot synopsis of movie.
        poster_image_url (str): Poster image url.
        trailer_youtube_url (str): Youtube trailer url.
	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, movie_image, trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_image
		self.trailer_youtube_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)




		