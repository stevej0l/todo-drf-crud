from rest_framework.decorators import api_view
from feature.musicapp.serializers.request_serializers import MusicRequestSerializer
from feature.musicapp.dataclasses.music_data import MusicData
from feature.musicapp.views import (
    list_songs,
    get_song,
    create_song,
    update_song,
    delete_song
)


@api_view(["GET", "POST"])
def music_controller(request):

    if request.method == "GET":
        return list_songs()

    serializer = MusicRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = MusicData(**serializer.validated_data)
    return create_song(data)

@api_view(["GET"])
def music_paginated_controller(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    return list_songs_paginated(page, page_size)


@api_view(["GET", "PUT", "DELETE"])
def music_detail_controller(request, pk):

    if request.method == "GET":
        return get_song(pk)

    if request.method == "PUT":
        serializer = MusicRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = MusicData(**serializer.validated_data)
        return update_song(pk, data)

    if request.method == "DELETE":
        return delete_song(pk)
