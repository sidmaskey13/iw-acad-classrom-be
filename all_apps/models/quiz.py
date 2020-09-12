from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    deadline_date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='quiz', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    title = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, related_name='quiz_questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizOptions(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, null=True, related_name='quiz_answers')
    option = models.CharField(max_length=100)
    correct = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.option


class QuizScoreData(models.Model):
    user = models.ForeignKey(User, related_name='quiz_data', on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, related_name='quiz_score_data', on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



