from rest_framework import serializers
from feature.artist.models import Artist


class ArtistResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
