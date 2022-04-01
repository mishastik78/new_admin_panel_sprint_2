from rest_framework import serializers

from movies.models import Filmwork


class FilmworkSerializer(serializers.ModelSerializer):
    actors = serializers.ListField()
    directors = serializers.ListField()
    writers = serializers.ListField()
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True, allow_null=True)

    class Meta:
        model = Filmwork
        fields = ('id', 'title', 'description', 'creation_date', 'rating',
                  'type', 'genres', 'actors', 'directors', 'writers')
