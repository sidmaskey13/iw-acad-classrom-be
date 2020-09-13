from django.contrib import admin
from ..models.assignment import AssignmentSubmit,AssignmentQuestion
from ..models.quiz import QuizScoreData,QuizOptions,QuizQuestion,Quiz
from ..models.comment import Comment
from ..models.post import Post
from ..models.like import Like
from ..models.authentication import UserDetail
# Register your models here.

admin.site.register(AssignmentSubmit)
admin.site.register(AssignmentQuestion)
admin.site.register(QuizScoreData)
admin.site.register(QuizOptions)
admin.site.register(QuizQuestion)
admin.site.register(Quiz)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(UserDetail)