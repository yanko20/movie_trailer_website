import media
import fresh_tomatoes

movie_ids = ["14002", "36819", "246741"]
movies = []
for id in movie_ids:
    movies.append(media.Movie(id))
fresh_tomatoes.open_movies_page(movies)