from django.urls import path
from rest_framework import routers

from all_apps.apis.quiz import QuizMainModelViewSet,\
    QuizQuestionModelViewSet, \
    QuizOptionsModelViewSet, \
    GetQuizQuestionView, \
    AddQuestion, \
    QuizScoreModelViewSet,ScoreEachQuizByStudent,ScoreEachQuizAllStudent

router = routers.DefaultRouter()
router.register('api/quiz', QuizMainModelViewSet, 'quiz')
router.register('api/quiz_question', QuizQuestionModelViewSet, 'quiz_question')
router.register('api/quiz_option', QuizOptionsModelViewSet, 'quiz_option')
router.register('api/quiz_score', QuizScoreModelViewSet, 'quiz_score')

urlpatterns = [
    path('api/quiz_question_option/<int:pk>/', GetQuizQuestionView.as_view()),
    path('api/quiz_question_add/', AddQuestion.as_view()),
    path('api/quiz_score_by_user/<int:pk>/', ScoreEachQuizByStudent.as_view()),
    path('api/quiz_score_all_user/<int:pk>/', ScoreEachQuizAllStudent.as_view()),
              ]+router.urls
