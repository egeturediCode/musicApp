from django.db import models
import os
from django.urls import reverse

# Create your models here.

class Song(models.Model):
    music_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    duration = models.DurationField(blank=True,null=True)
    image = models.ImageField(upload_to='img/songs/')
    audio_file = models.FileField(upload_to='audio/')
    is_fav = models.BooleanField(default = False)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        if self.audio_file and os.path.isfile(self.audio_file.path):
            os.remove(self.audio_file.path)
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return f"{self.music_name} - {self.artist_name}"

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='playlists',blank=True)
    image = models.ImageField(upload_to='img/playlists/',blank=True)
    description = models.CharField(max_length=150,blank=True)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('playlist_detail', args=[self.id]) # reverse fonksiyonu playlist_detail isimli urli alır değişkene self.id'yi koyar.
    
    def __str__(self):
        return self.name
    
class Genres (models.Model):
    name = models.CharField(max_length = 25)
    is_showed = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    

    
