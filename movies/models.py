from django.db import models

class Genre(models.Model):  # NUEVO
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # minutos
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    genres = models.ManyToManyField(Genre, related_name='movies')  # NUEVO

    def __str__(self):
        return self.title