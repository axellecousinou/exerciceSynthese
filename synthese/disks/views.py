from django.shortcuts import render
from .models import Album


def accueil(request):
    return render(request, 'disks/accueil.html', {'albums': Album.objects.all()})
