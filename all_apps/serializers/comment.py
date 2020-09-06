from rest_framework import serializers

from all_apps.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
