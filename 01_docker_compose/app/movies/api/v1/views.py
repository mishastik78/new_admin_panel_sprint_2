from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from rest_framework import viewsets

from movies.models import Filmwork

from .serializers import FilmworkSerializer


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FilmworkSerializer
    queryset = Filmwork.objects.annotate(
        actors=ArrayAgg('persons__full_name', filter=Q(film_crew__role='actor'), distinct=True),
        directors=ArrayAgg('persons__full_name', filter=Q(film_crew__role='director'), distinct=True),
        writers=ArrayAgg('persons__full_name', filter=Q(film_crew__role='writer'), distinct=True),
    ).prefetch_related('genres')
