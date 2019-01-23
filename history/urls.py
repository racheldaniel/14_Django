from django.urls import path

from . import views


app_name = "history"
urlpatterns = [
    path('', views.artists, name='artists'),
    path('<int:artist_id>/', views.detail, name='detail'),
    path('<int:artist_id>/addSong', views.add_song, name='add_song'),
    path('<int:artist_id>/addAlbum', views.add_album, name='add_album')

]