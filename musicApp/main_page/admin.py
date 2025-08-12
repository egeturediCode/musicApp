from django.contrib import admin
from .models import Genres,Song,Playlist
# Register your models here.

admin.site.register(Genres)
admin.site.register(Song)
admin.site.register(Playlist)