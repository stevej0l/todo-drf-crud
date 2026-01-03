from django.urls import path
from feature.artist.controllers.artist_controller import (
    artist_controller,
    artist_detail_controller,
    artist_songs_controller,
)

urlpatterns = [
    path("", artist_controller),
    path("<int:pk>/", artist_detail_controller),
    path("<int:pk>/songs/", artist_songs_controller),
]
