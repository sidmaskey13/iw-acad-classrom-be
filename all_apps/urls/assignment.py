from rest_framework import routers
from django.urls import path

from all_apps.apis.assignment import AssignmentQuestionModelViewSet, AssignmentSubmitModelViewSet,GetAllAssignemntView

router = routers.DefaultRouter()
router.register('api/assignment_question', AssignmentQuestionModelViewSet, 'assignment_question')
router.register('api/assignment_submit', AssignmentSubmitModelViewSet, 'assignment_submit')

urlpatterns = [
    path('api/assignment_submit_by_question/<int:pk>/', GetAllAssignemntView.as_view()),
              ]+router.urls
