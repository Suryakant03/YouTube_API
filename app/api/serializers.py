from rest_framework import serializers

from core.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """Serializer for Video objects"""

    class Meta:
        model = Video
        fields = "__all__"
