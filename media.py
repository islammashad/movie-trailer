
import webbrowser

""" This class is used to  store movie related information

    Attributes:

        title: The title of the movie
        storyline: A short description of what the movie is about
        poster_image_url: The URL address of a poster of the movie
        trailer_youtube_url: A link to a YouTube.com page that shows
        the trailer of the movie """


class Movie():    
    # This is The Constructor for Intializing the data
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function for showing Our Trailer     
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
      