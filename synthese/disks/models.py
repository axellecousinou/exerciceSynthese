from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=25, decimal_places=2)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    composer = models.CharField(max_length=200)

    def __str__(self):
        return self.name
