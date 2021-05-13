from django.shortcuts import render
from .models import Album, Track
from .forms import SearchForm


def accueil(request):
    valid = False
    form = SearchForm(request.POST or None)
    list = []
    if form.is_valid():
        text = form.cleaned_data['text']
        if text=="":
            list = Album.objects.all()
        else:
            list = Album.objects.filter(title__contains=text)
        valid = True
        return render(request, 'disks/accueil.html', {'albums': list, 'valid': valid, 'form': form})
    return render(request, 'disks/accueil.html', {'albums': Album.objects.all(), 'valid': valid, 'form': form})


def list_tracks(request, album_id):
    list = Track.objects.filter(album_id=album_id)
    return render(request, 'disks/list_tracks.html', {'album_tracks': list, 'album_name':
        Album.objects.get(id=album_id).title, 'artist': Album.objects.get(id=album_id).artist.name})

