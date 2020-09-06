from rest_framework import serializers

from all_apps.models import Like


class LikeSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = '__all__'
