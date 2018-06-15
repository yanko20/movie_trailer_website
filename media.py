"""media module defines different types of media"""
import requests
# import json


class Movie():
    """Movies class whose instances represent a single movie
    Attributes:
        title: Movie title
        poster_image_url: Movie poster image link
        trailer_youtube_url: Movie youtube trailer
    """

    api_key = "33b6d39594c9f8eca8b330f81b49c2d9"

    def __init__(self, movie_id):
        """Initiates Movie class instance"""
        self.movie_id = movie_id
        self.title = self.title()
        self.poster_image_url = self.poster_image_url()
        self.trailer_youtube_url = self.trailer_youtube_url()

    def movie_api_url(self):
        """"Constructs and returns TMDb movie api url"""
        return "https://api.themoviedb.org/3/movie/{}?api_key={}" \
            .format(self.movie_id, Movie.api_key)

    def config_api_url(self):
        """"Constructs and returns TMDb configuration api url"""
        return "https://api.themoviedb.org/3/configuration?api_key={}" \
            .format(Movie.api_key)

    def movie_json(self):
        """"Returns TMDb movie json response"""
        return requests.get(self.movie_api_url()).json()

    def config_json(self):
        """"Returns TMDb configuration json response"""
        return requests.get(self.config_api_url()).json()

    def title(self):
        """"Returns movie title"""
        return self.movie_json()["original_title"]

    def poster_image_url(self):
        """"Returns poster image url"""
        base_url = self.config_json()["images"]["base_url"]
        poster_path = self.movie_json()["poster_path"]
        poster_url = base_url + "original{}".format(poster_path)
        return poster_url

    def trailer_youtube_url(self):
        """"Returns movie trailer youtube url"""
        video_api_url = \
            "https://api.themoviedb.org/3/movie/{}/videos?api_key={}" \
            .format(self.movie_id, Movie.api_key)
        video_api_url = video_api_url.format(self.movie_id)
        json = requests.get(video_api_url).json()
        youtube_id = json["results"][0]["key"]
        youtube_url = "https://www.youtube.com/watch?v={}".format(youtube_id)
        return youtube_url  # NOQA
