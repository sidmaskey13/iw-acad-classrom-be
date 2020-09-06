from django.contrib.auth import get_user_model
from django.db import models

from all_apps.models.post import Post

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
