"""Blueprint for a movie which includes name, poster image, trailer link, and imdb link"""
class Movie():
    def __init__(self,movie_title,imdb_link, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.imdblink = imdb_link
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
