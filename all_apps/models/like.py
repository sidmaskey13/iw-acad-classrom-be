from django.contrib.auth import get_user_model
from django.db import models

from all_apps.models.post import Post

User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE, null=True)
    count = models.IntegerField()


