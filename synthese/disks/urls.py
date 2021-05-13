from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('list-tracks/<int:album_id>', views.list_tracks, name="list_tracks"),
]
