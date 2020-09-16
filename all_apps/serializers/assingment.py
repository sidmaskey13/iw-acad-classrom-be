from django.contrib.auth import get_user_model
from rest_framework import serializers

from all_apps.models import AssignmentQuestion, AssignmentSubmit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()


class AssignmentQuestionSerializer(serializers.ModelSerializer):
    submission_count = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = AssignmentQuestion
        fields = '__all__'

    def get_submission_count(self, obj):
        return obj.assignment_submissions.count()

    def get_status(self, obj):
        user = self.context['request'].user
        return obj.assignment_submissions.filter(user=user.id).count()


class AssignmentSubmitSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AssignmentSubmit
        fields = '__all__'



