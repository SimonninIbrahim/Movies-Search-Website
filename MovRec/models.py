from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length = 255, null=True, blank=True)
    year = models.IntegerField(validators=[
            MinValueValidator(1890)
        ],null=True, blank=True)
    runtime = models.CharField(max_length = 255, null=True, blank=True)
    genre = models.CharField(max_length = 255, null=True, blank=True)
    director = models.CharField(max_length = 255, null=True, blank=True)
    cast = models.CharField(max_length = 255, null=True, blank=True)
    imdbRating = models.FloatField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ], null=True, blank=True)
    imdbVotes = models.IntegerField(null=True, blank=True)
    poster = models.CharField(max_length = 2083, null=True, blank=True)
    fullplot = models.TextField(max_length = 3000, null=True, blank=True)
    language = models.CharField(max_length = 255, null=True, blank=True)
    country = models.CharField(max_length = 255, null=True, blank=True)
    awards = models.CharField(max_length = 255, null=True, blank=True)

    # a method to replace the null values with default values
    def save(self, *args, **kwargs):
        if self.title is None:
            self.title = "Untitled"

        if self.director is None:
            self.director = "Unknown"

        if self.cast is None:
            self.cast = "Unknown"

        if self.imdbRating is None:
            self.imdbRating = 0

        if self.imdbVotes is None:
            self.imdbVotes = 0

        if self.poster is None:
            self.poster = "https://png.pngtree.com/background/20210711/original/pngtree-film-and-television-festival-auditorium-shows-airport-board-poster-picture-image_1105016.jpg"

        if self.fullplot is None:
            self.fullplot = "-"

        if self.language is None:
            self.language = "-"

        if self.country is None:
            self.country = "-"

        super().save(*args, **kwargs)

    # a method to make the object appear as a movie name alongside its year
    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title