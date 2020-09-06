from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_detail')
    profile_pic = models.ImageField(null=True, blank=True)
