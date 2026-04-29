from django.contrib import admin
from .models import Movie, Genre  # CAMBIO

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date')

@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')