from rest_framework import serializers

class ArtistRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    genre = serializers.CharField()
    country = serializers.CharField()
