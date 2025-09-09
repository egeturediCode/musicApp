from django.urls import path
from . import views
#http://127.0.0.1:8000/               =>main
#http://127.0.0.1:8000/index          =>main
#http://127.0.0.1:8000/genre          =>genres  
#http://127.0.0.1:8000/playlist/#     =>playlist
#http://127.0.0.1:8000/addplaylist    =>addplaylist


urlpatterns = [
    path("",  views.main_page, name="index"),
    path("index",  views.main_page, name="index"),
    path('playlist/<int:playlist_id>/', views.playlist_page, name='playlist_detail'),
    path("genres", views.genres),
    path("playlists", views.playlists),
    path("live/", views.live),
    path("favourites", views.favourites),
    path("explore", views.explore),
    path("artists", views.artists),
    path("albums", views.albums),
    path('toggle-fav/<int:song_id>/', views.toggle_favorite, name='toggle_favorite'),
    
]
