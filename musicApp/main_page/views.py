from django.http.response import HttpResponse
from django.http import JsonResponse
from main_page.models import Genres,Playlist,Song
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlaylistForm
import random
from random import shuffle, choice

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.


def toggle_favorite(request, song_id):
    if request.method == "POST":
        song = get_object_or_404(Song, id=song_id)
        song.is_fav = not song.is_fav 
        song.save()
        return JsonResponse({'is_fav': song.is_fav})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def play_music(request, song_id):
    if request.method == "POST":
        song = get_object_or_404(Song, id=song_id)
        song.is_fav = not song.is_fav 
        song.save()
        return JsonResponse({'is_fav': song.is_fav})
    return JsonResponse({'error': 'Invalid request'}, status=400)


#-------------------------------------------------------------------------------------

@login_required(login_url='/user/login')
def main_page(request):
    selected_main = Playlist.objects.filter(name ="Top Songs").first()
    trending = Playlist.objects.filter(name = "Trending").first()
    trending_list = list(trending.songs.all())
    songs = Song.objects.all()

    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Trending": random.choice(trending_list),
        "Genres": Genres.objects.all(),
        "Playlist3": Playlist.objects.all()[:4],
        "Selected_playlist": selected_main,
        "SongAll" : songs,
        "form": form
        
    }
    return render(request, "index.html",content)

@login_required(login_url='/user/login')
def playlist_page(request, playlist_id=None):
    selected = Playlist.objects.filter(id=playlist_id).first()
    
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            form.save()
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "PlaylistAll": Playlist.objects.all(),
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "Selected_playlist": selected,
        "form": form

        
    }
    return render(request,"playlist.html",content)

@login_required(login_url='/user/login')
def playlists(request, playlist_id=None):
    selected = Playlist.objects.filter(id=playlist_id).first()
    trending = Playlist.objects.filter(name = "Trending").first()

    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "PlaylistAll": Playlist.objects.all(),
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "Selected_playlist": selected,
        "form": form,
        "trending": trending,
      
    }
    return render(request,"playlists.html",content)

@login_required(login_url='/user/login')
def genres(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            form.save()
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Genres": Genres.objects.all(),
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "form": form

    }
    return render(request,"genres.html",content)

@login_required(login_url='/user/login')
def albums(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "form": form

    }
    return render(request,"albums.html",content)

@login_required(login_url='/user/login')
def artists(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "form": form

    }
    return render(request,"artists.html",content)

@login_required(login_url='/user/login')
def explore(request):
    songs = Song.objects.all()
    # the songs to get a random selection according to the selected artist
    artists = Song.objects.values_list('artist_name', flat=True).distinct()
    selected_artist = choice(list(artists))
    for_x_fans = Song.objects.filter(artist_name=selected_artist).all()

    new_releases = Song.objects.all().order_by('-id')[:6]

    random_songs = Song.objects.order_by('?')[:6]

    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Playlist3": Playlist.objects.all()[:4],
        "SongAll" : songs,
        "form": form,
        "for_x_fans": for_x_fans,
        "new_releases": new_releases,
        "random_songs": random_songs,
    }
    return render(request,"explore.html",content)

@login_required(login_url='/user/login')
def favourites(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "Fav_songs" : Song.objects.filter(is_fav = True),
        "form": form

    }
    return render(request,"favourites.html",content)

@login_required(login_url='/user/login')
def live(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    content = {
        "Playlist3": Playlist.objects.all()[:4],
        "Song": Song.objects.all(),
        "form": form

    }
    return render(request,"live.html",content)






def playlist_list(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save()
            return redirect(playlist.get_absolute_url())
    else:
        form = PlaylistForm()

    playlists = Playlist.objects.prefetch_related('songs').all()
    return render(request, 'playlist_list.html', {'playlists': playlists,'form': form})
