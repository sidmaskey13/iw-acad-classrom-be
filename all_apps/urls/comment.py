from rest_framework import routers

from all_apps.apis.comment import CommentModelViewSet

router = routers.DefaultRouter()
router.register('api/comment', CommentModelViewSet, 'comments')

urlpatterns = router.urls
