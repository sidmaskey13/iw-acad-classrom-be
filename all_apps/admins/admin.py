from django.contrib import admin
from ..models.assignment import AssignmentSubmit,AssignmentQuestion
from ..models.quiz import QuizScoreData,QuizOptions,QuizQuestion,Quiz
from ..models.comment import Comment
from ..models.post import Post
from ..models.like import Like
from ..models.authentication import UserDetail
# Register your models here.

admin.site.register(AssignmentSubmit,AssignmentSubmit,AssignmentQuestion,Quiz,QuizQuestion,QuizOptions,QuizScoreData,Comment,Post,Like,UserDetail)