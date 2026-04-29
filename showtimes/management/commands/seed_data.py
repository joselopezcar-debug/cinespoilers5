from django.core.management.base import BaseCommand
from movies.models import Movie, Genre
from showtimes.models import Showtime
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Seed de datos iniciales'

    def handle(self, *args, **kwargs):
        # Crear géneros
        genres_names = ['Acción', 'Drama', 'Comedia', 'Terror', 'Sci-Fi']

        genres = []
        for name in genres_names:
            genre, _ = Genre.objects.get_or_create(name=name)
            genres.append(genre)

        # Crear películas
        movies = []
        for i in range(5):
            movie, _ = Movie.objects.get_or_create(
                title=f"Pelicula {i+1}",
                defaults={
                    'description': 'Descripción de prueba',
                    'duration': random.randint(90, 150),
                    'release_date': '2024-01-01'
                }
            )
            movie.genres.set(random.sample(genres, k=2))
            movies.append(movie)

        # Crear funciones
        for movie in movies:
            for i in range(3):
                Showtime.objects.create(
                    movie=movie,
                    start_time=datetime.now() + timedelta(days=i),
                    room=f"Sala {random.randint(1,5)}",
                    price=random.randint(10, 30)
                )

        self.stdout.write(self.style.SUCCESS('Data generada correctamente'))