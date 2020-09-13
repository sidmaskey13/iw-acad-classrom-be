from rest_framework import serializers

from all_apps.models import Post
from all_apps.serializers import ProfilePicSerializer
from all_apps.serializers.comment import CommentSerializer
from all_apps.serializers.like import LikeSerializer


class PostSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)
    userProfile = ProfilePicSerializer(source='user.profile_pic', read_only=True)
    comments = CommentSerializer(source='post_comments', read_only=True,many=True)
    likes = LikeSerializer(source='post_likes', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class PostOwnSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
