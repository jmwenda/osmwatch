from django.db import models
from cities.models import City
class CityDetail(City):
    min_lat = models.CharField(max_length=20)
    max_lon = models.CharField(max_length=20)
    min_lon = models.CharField(max_length=20)
    max_lat = models.CharField(max_length=20)
class Changeset(models.Model):
    flag = models.BooleanField()
    ekip = models.CharField(max_length=10)
    osm_username = models.CharField(max_length=20)
    changesetid = models.CharField(max_length=20)
    editor = models.CharField(max_length=20)
    comment = models.TextField()
    datetime = models.DateTimeField()
