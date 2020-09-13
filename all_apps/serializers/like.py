from rest_framework import serializers

from all_apps.models import Like


class LikeSerializer(serializers.ModelSerializer):
    # countAdd = serializers.IntegerField(read_only=True)

    class Meta:
        model = Like
        fields = ('post','count')
