from rest_framework import serializers

class MusicRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    duration = serializers.IntegerField()
    release_date = serializers.DateField()
    artist_id = serializers.IntegerField()
