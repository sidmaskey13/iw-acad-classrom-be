from rest_framework import routers

from all_apps.apis.post import PostModelViewSet

router = routers.DefaultRouter()
router.register('api/post', PostModelViewSet, 'posts')

urlpatterns = router.urls
