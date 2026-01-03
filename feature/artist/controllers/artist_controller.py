from rest_framework.decorators import api_view
from feature.artist.serializers.request_serializers import ArtistRequestSerializer
from feature.artist.dataclasses.artist_data import ArtistData
from feature.artist.views import list_artist_songs
from feature.artist.views import (
    list_artists,
    get_artist,
    create_artist,
    update_artist,
    delete_artist
)
@api_view(["GET"])
def artist_songs_controller(request, pk):
    return list_artist_songs(pk)

@api_view(["GET", "POST"])
def artist_controller(request):

    if request.method == "GET":
        return list_artists()

    serializer = ArtistRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = ArtistData(**serializer.validated_data)
    return create_artist(data)


@api_view(["GET", "PUT", "DELETE"])
def artist_detail_controller(request, pk):

    if request.method == "GET":
        return get_artist(pk)

    if request.method == "PUT":
        serializer = ArtistRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ArtistData(**serializer.validated_data)
        return update_artist(pk, data)

    if request.method == "DELETE":
        return delete_artist(pk)
