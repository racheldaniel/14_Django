from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    year_est = models.IntegerField()

    def __str__(self):
        return self.artist_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=20)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name



