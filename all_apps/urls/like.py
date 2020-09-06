from rest_framework import routers

from all_apps.apis.like import LikeModelViewSet

router = routers.DefaultRouter()
router.register('api/like', LikeModelViewSet, 'likes')

urlpatterns = router.urls
