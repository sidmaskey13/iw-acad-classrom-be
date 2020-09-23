from rest_framework import serializers

from all_apps.models import Post
from all_apps.serializers import ProfilePicSerializer
from all_apps.serializers.comment import CommentSerializer
from all_apps.serializers.like import LikeSerializer


class PostSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)
    userProfile = ProfilePicSerializer(source='user.profile_pic', read_only=True)
    comments = CommentSerializer(source='post_comments', read_only=True,many=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.post_likes.count()

class PostOwnSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
