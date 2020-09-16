from rest_framework.response import Response
from rest_framework.views import APIView

from all_apps.models import AssignmentQuestion, AssignmentSubmit

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from all_apps.serializers import QuizQuestionSerializer
from all_apps.serializers.assingment import AssignmentQuestionSerializer, AssignmentSubmitSerializer
from rest_framework.parsers import FileUploadParser


class AssignmentQuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentQuestionSerializer
    permission_classes = [IsAuthenticated]
    queryset = AssignmentQuestion.objects.all().order_by('-id')
    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def destroy(self, request, *args, **kwargs):
        serializer = AssignmentQuestionSerializer(instance=self.get_object())
        if self.request.user.id == serializer.data['user']:
            self.get_object().delete()
            return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class AssignmentSubmitModelViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmitSerializer
    permission_classes = [IsAuthenticated]
    queryset = AssignmentSubmit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        serializer = AssignmentSubmitSerializer(instance=self.get_object())
        if self.request.user.id == serializer.data['user']:
            self.get_object().delete()
            return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class GetAllAssignemntView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        obj_id = kwargs['pk']
        data = AssignmentSubmit.objects.filter(assignment=obj_id)
        serializer = AssignmentSubmitSerializer(instance=data, many=True)
        return Response({'result':serializer.data})


class GetAllOwnAssignemntView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        data = AssignmentSubmit.objects.filter(user=self.request.user)
        serializer = AssignmentSubmitSerializer(instance=data, many=True)
        return Response({'result':serializer.data})


class CheckSubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        data = AssignmentSubmit.objects.filter(user=self.request.user)
        serializer = AssignmentSubmitSerializer(instance=data, many=True)
        return Response({'result':serializer.data})





