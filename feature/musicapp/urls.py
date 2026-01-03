from django.urls import path
from feature.musicapp.controllers.music_controller import (
    music_controller,
    music_detail_controller,
    music_paginated_controller,
)

urlpatterns = [
    path("", music_controller),
    path("<int:pk>/", music_detail_controller),
    path("paginated/", music_paginated_controller),
]
