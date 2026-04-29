from rest_framework import viewsets
from .models import Movie, Genre  # CAMBIO
from .serializers import MovieSerializer, GenreSerializer  # CAMBIO


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):  # NUEVO
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer