from rest_framework.response import Response
from rest_framework.views import APIView

from all_apps.models import Quiz, QuizQuestion, QuizOptions, QuizScoreData

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAdminUser

from all_apps.serializers.quiz import QuizSerializer, QuizOptionsSerializer, QuizScoreDataSerializer, \
    QuizQuestionSerializer, QuizScoreAllUserDataSerializer


class QuizMainModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def destroy(self, request, *args, **kwargs):
    #     serializer = QuizSerializer(instance=self.get_object())
    #     if self.request.user.id == serializer.data['user']:
    #         self.get_object().delete()
    #         return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class QuizQuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuizQuestionSerializer
    permission_classes = [IsAuthenticated]
    queryset = QuizQuestion.objects.all()


class QuizOptionsModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuizOptionsSerializer
    permission_classes = [IsAuthenticated]
    queryset = QuizOptions.objects.all()


class GetQuizQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj_id = kwargs['pk']
        data = QuizQuestion.objects.filter(quiz=obj_id)
        serializer = QuizQuestionSerializer(instance=data, many=True)
        return Response({'result': serializer.data})


class AddQuestion(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        for q in request.data:
            serializerQuestion = QuizQuestionSerializer(data={'quiz': q.get('quiz'),
                                                              'title': q.get('question')})
            serializerQuestion.is_valid(raise_exception=True)
            serializerQuestion.save()

            serializerOption1 = QuizOptionsSerializer(
                data={'option': q.get('option1'),
                      'correct': q.get('option1_correct'), 'question': serializerQuestion.data['id']})
            serializerOption1.is_valid(raise_exception=True)
            serializerOption1.save()

            serializerOption2 = QuizOptionsSerializer(
                data={'option': q.get('option2'),
                      'correct': q.get('option2_correct'), 'question': serializerQuestion.data['id']})
            serializerOption2.is_valid(raise_exception=True)
            serializerOption2.save()

            serializerOption3 = QuizOptionsSerializer(
                data={'option': q.get('option3'),
                      'correct': q.get('option3_correct'), 'question': serializerQuestion.data['id']})
            serializerOption3.is_valid(raise_exception=True)
            serializerOption3.save()

            serializerOption4 = QuizOptionsSerializer(
                data={'option': q.get('option4'),
                      'correct': q.get('option4_correct'), 'question': serializerQuestion.data['id']})
            serializerOption4.is_valid(raise_exception=True)
            serializerOption4.save()

        return Response({'result': serializerQuestion.data})


class QuizScoreModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuizScoreDataSerializer
    permission_classes = [IsAuthenticated]
    queryset = QuizScoreData.objects.all()
    # permission_classes = [IsAdminUser,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScoreEachQuizByStudent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj_id = kwargs['pk']
        data = QuizScoreData.objects.filter(quiz=obj_id, user=self.request.user)
        serializer = QuizScoreDataSerializer(instance=data, many=True)
        return Response({'result': serializer.data})


class ScoreEachQuizAllStudent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj_id = kwargs['pk']
        data = QuizScoreData.objects.filter(quiz=obj_id)
        serializer = QuizScoreAllUserDataSerializer(instance=data, many=True)
        return Response({'result': serializer.data})


