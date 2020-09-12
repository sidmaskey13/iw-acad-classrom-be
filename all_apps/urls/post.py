from django.urls import path
from rest_framework import routers
from all_apps.apis.post import PostModelViewSet,OwnPostView

router = routers.DefaultRouter()
router.register('api/post', PostModelViewSet, 'posts')

urlpatterns = [
    path('api/own_post', OwnPostView.as_view()),
              ]+router.urls
