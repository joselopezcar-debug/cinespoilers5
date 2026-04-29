from django.db import models
from movies.models import Movie  # NUEVO

class Showtime(models.Model):  # NUEVO
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    room = models.CharField(max_length=50)  # Ej: Sala 1, Sala VIP
    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"