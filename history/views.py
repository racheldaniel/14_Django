from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
from .models import Song

def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    context = {'artist_list': artist_list}
    return render(request, 'history/artists.html', context)

def detail(request, artist_id):
    artist = Artist.objects.filter(id = artist_id)
    song_list = Song.objects.filter(artist_id = artist_id)
    context = {'song_list': song_list, 'artist': artist}
    return render(request, 'history/detail.html', context)