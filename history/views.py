from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song, Album


def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    context = {'artist_list': artist_list}
    return render(request, 'history/artists.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    song_list = Song.objects.filter(artist_id = artist_id)
    context = {'song_list': song_list, 'artist': artist}
    return render(request, 'history/detail.html', context)

def add_song(request, artist_id):
    print("artist id:", artist_id)
    album = get_object_or_404(Album, pk=request.POST["album"])
    artist = get_object_or_404(Artist, pk=artist_id)
    new_song = Song(song_name=request.POST["song_name"], album=album, artist=artist)
    new_song.save()
    return HttpResponseRedirect(reverse('history:detail', args=(artist.id, )))