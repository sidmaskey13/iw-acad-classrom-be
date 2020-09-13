from django.urls import path
from rest_framework import routers

from all_apps.apis.like import LikeAddView

urlpatterns = [
    path('api/add_like', LikeAddView.as_view())]
