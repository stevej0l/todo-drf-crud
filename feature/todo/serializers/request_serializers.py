from rest_framework import serializers


class TodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(default=False)
