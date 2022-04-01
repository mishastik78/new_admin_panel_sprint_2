# Generated by Django 3.2 on 2022-03-28 16:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_filmwork_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, db_index=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, db_index=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_crew', to='movies.filmwork'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('director', 'director'), ('actor', 'actor'), ('writer', 'writer')], max_length=50, verbose_name='role'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['film_work', 'person'], name='film_work_person'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='film_work_genre'),
        ),
    ]