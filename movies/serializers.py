from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(  # CAMBIO IMPORTANTE
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):  # NUEVO
        representation = super().to_representation(instance)
        representation['genres'] = GenreSerializer(instance.genres.all(), many=True).data
        return representation