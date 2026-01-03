from rest_framework import serializers
from feature.musicapp.models import Music
from feature.artist.serializers.response_serializers import ArtistResponseSerializer


class MusicResponseSerializer(serializers.ModelSerializer):
    artist = ArtistResponseSerializer()

    class Meta:
        model = Music
        fields = "__all__"
