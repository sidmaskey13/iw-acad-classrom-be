from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class AssignmentQuestion(models.Model):
    title = models.CharField(max_length=200)
    deadline_date = models.DateTimeField()
    file = models.FileField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='assignment_question', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AssignmentSubmit(models.Model):
    assignment = models.ForeignKey(AssignmentQuestion, on_delete=models.SET_NULL, null=True, related_name='assignment_submissions')
    file = models.FileField(null=True, blank=True)
    link = models.CharField(null=True, blank=True, max_length=200)
    user = models.ForeignKey(User, related_name='assignment_submit', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


