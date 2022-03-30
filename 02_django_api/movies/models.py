import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(
        _('fullname'),
        max_length=255,
        db_index=True,
    )

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):

    class MovieType(models.TextChoices):
        MOVIE = 'movie', _('movie')
        TVSHOW = 'tv_show', _('tvshow')

    title = models.CharField(
        _('title'),
        max_length=255,
        db_index=True,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )
    creation_date = models.DateField(
        _('creation_date'),
        blank=True,
        db_index=True,
    )
    rating = models.FloatField(
        _('rating'),
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        db_index=True,
    )
    type = models.CharField(
        _('type'),
        max_length=50,
        choices=MovieType.choices,
    )
    genres = models.ManyToManyField(
        Genre,
        through='GenreFilmwork',
    )
    persons = models.ManyToManyField(
        Person,
        through='PersonFilmwork',
    )
    file_path = models.FileField(
        _('file'),
        blank=True,
        null=True,
        upload_to='movies/',
    )

    class Meta:
        ordering = ('-created',)
        db_table = "content\".\"film_work"
        verbose_name = _('film')
        verbose_name_plural = _('films')

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey(
        Filmwork,
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "content\".\"genre_film_work"
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'genre'],
                name='film_work_genre',
            ),
        ]


class PersonFilmWork(UUIDMixin):

    class PersonRole(models.TextChoices):
        DIRECTOR = 'director', _('director')
        ACTOR = 'actor', _('actor')
        WRITER = 'writer', _('writer')

    film_work = models.ForeignKey(
        Filmwork,
        on_delete=models.CASCADE,
        related_name='film_crew',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        _('role'),
        max_length=50,
        choices=PersonRole.choices,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "content\".\"person_film_work"
        indexes = [
            models.Index(
                fields=['film_work', 'person'],
                name='film_work_person',
            )
        ]
