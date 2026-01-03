from feature.artist.models import Artist
from feature.artist.serializers.response_serializers import ArtistResponseSerializer
from feature.common.utils.responses import serialized_response, success_response
from rest_framework import status
from feature.musicapp.models import Music
from feature.musicapp.serializers.response_serializers import MusicResponseSerializer
from feature.common.utils.responses import serialized_response


@serialized_response(MusicResponseSerializer, many=True)
def list_artist_songs(artist_id):
    return Music.objects.filter(artist_id=artist_id)

# ---------- READ ----------

@serialized_response(ArtistResponseSerializer, many=True)
def list_artists():
    return Artist.objects.all()


@serialized_response(ArtistResponseSerializer)
def get_artist(artist_id):
    return Artist.objects.get(id=artist_id)


# ---------- WRITE ----------

def create_artist(data):
    artist = Artist.create_artist(data)
    serializer = ArtistResponseSerializer(artist)
    return success_response(
        data=serializer.data,
        message="Artist created successfully",
        status_code=status.HTTP_201_CREATED
    )


def update_artist(artist_id, data):
    artist = Artist.update_artist(artist_id, data)
    serializer = ArtistResponseSerializer(artist)
    return success_response(
        data=serializer.data,
        message="Artist updated successfully"
    )


def delete_artist(artist_id):
    Artist.delete_artist(artist_id)
    return success_response(
        message="Artist deleted successfully",
        status_code=status.HTTP_204_NO_CONTENT
    )
