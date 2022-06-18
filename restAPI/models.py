from django.db import models

# Create your models here.
class Movies((models.Model)):
    movie_name = models.CharField(max_length=30)
    movie_year = models.IntegerField()

    def __str__(self):
        return self.movie_name
