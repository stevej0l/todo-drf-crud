from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API entry point
    path("api/artists/", include("feature.artist.urls")),
    path("api/songs/", include("feature.musicapp.urls")),
]
