from feature.musicapp.models import Music
from feature.common.utils.pagination import paginate_queryset
from feature.common.utils.responses import success_response
from feature.musicapp.serializers.response_serializers import MusicResponseSerializer
from feature.common.utils.responses import serialized_response, success_response
from rest_framework import status


@serialized_response(MusicResponseSerializer, many=True)
def list_songs():
    return Music.objects.select_related("artist").all()


@serialized_response(MusicResponseSerializer)
def get_song(song_id):
    return Music.objects.get(id=song_id)


def create_song(data):
    song = Music.create_song(data)
    serializer = MusicResponseSerializer(song)
    return success_response(
        data=serializer.data,
        message="Song created successfully",
        status_code=status.HTTP_201_CREATED
    )


def update_song(song_id, data):
    song = Music.update_song(song_id, data)
    serializer = MusicResponseSerializer(song)
    return success_response(
        data=serializer.data,
        message="Song updated successfully"
    )


def delete_song(song_id):
    Music.delete_song(song_id)
    return success_response(
        message="Song deleted successfully",
        status_code=status.HTTP_204_NO_CONTENT
    )

def list_songs_paginated(page, page_size):
    queryset = Music.objects.select_related("artist").all()
    result = paginate_queryset(queryset, page, page_size)

    serializer = MusicResponseSerializer(result["items"], many=True)

    return success_response(
        data=serializer.data,
        pagination=result["pagination"]
    )