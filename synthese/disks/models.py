from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=None, decimal_places=2)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    composer = models.CharField(max_length=200)
