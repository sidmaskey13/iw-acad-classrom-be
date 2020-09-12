from rest_framework import serializers

from all_apps.models import Quiz, QuizQuestion, QuizScoreData, QuizOptions


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizScoreDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizScoreData
        fields = '__all__'


class QuizScoreAllUserDataSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = QuizScoreData
        fields = '__all__'


class QuizOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOptions
        fields = '__all__'



class QuizQuestionSerializer(serializers.ModelSerializer):
    options = QuizOptionsSerializer(source='quiz_answers', read_only=True, many=True)

    class Meta:
        model = QuizQuestion
        fields = '__all__'





