from rest_framework.response import Response

from all_apps.models import Like

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from all_apps.serializers.like import LikeSerializer


class LikeModelViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        serializer = LikeSerializer(instance=self.get_object())
        if self.request.user.id == serializer.data['user']:
            self.get_object().delete()
            return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
