from rest_framework import serializers
from .models import Movie, Genre  # CAMBIO


class GenreSerializer(serializers.ModelSerializer):  # NUEVO
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # CAMBIO

    class Meta:
        model = Movie
        fields = '__all__'