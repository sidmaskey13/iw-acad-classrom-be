from rest_framework.response import Response
from rest_framework.views import APIView

from all_apps.models import Quiz, QuizQuestion, QuizOptions, QuizScoreData

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from all_apps.serializers.quiz import QuizSerializer, QuizOptionsSerializer, QuizScoreDataSerializer, QuizQuestionSerializer


class QuizMainModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        serializer = QuizSerializer(instance=self.get_object())
        if self.request.user.id == serializer.data['user']:
            self.get_object().delete()
            return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


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

    def get(self,request,*args,**kwargs):
        obj_id = kwargs['pk']
        data = QuizQuestion.objects.filter(quiz=obj_id)
        serializer = QuizQuestionSerializer(instance=data, many=True)
        return Response({'result':serializer.data})
