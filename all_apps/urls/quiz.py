from rest_framework import routers

from all_apps.apis.quiz import QuizMainModelViewSet, QuizQuestionModelViewSet, QuizOptionsModelViewSet

router = routers.DefaultRouter()
router.register('api/quiz', QuizMainModelViewSet, 'quiz')
router.register('api/quiz_question', QuizQuestionModelViewSet, 'quiz_question')
router.register('api/quiz_option', QuizOptionsModelViewSet, 'quiz_option')

urlpatterns = router.urls
