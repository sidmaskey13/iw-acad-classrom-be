from rest_framework import serializers

from all_apps.models import AssignmentQuestion, AssignmentSubmit


class AssignmentQuestionSerializer(serializers.ModelSerializer):
    submission_count = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = AssignmentQuestion
        fields = '__all__'

    def get_submission_count(self, obj):
        return obj.assignment_submissions.count()

    def get_status(self, obj):
        return obj.assignment_submissions.filter(user=self.request.user)


class AssignmentSubmitSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AssignmentSubmit
        fields = '__all__'



