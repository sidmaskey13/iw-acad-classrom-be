from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from all_apps.models import Like

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from all_apps.serializers.like import LikeSerializer


class LikeAddView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializerQuestion = LikeSerializer(data={'count': request.data.get('countAdd'), 'post': request.data.get('post')})
        serializerQuestion.is_valid(raise_exception=True)
        # serializerQuestion.save()
        postId = int(serializerQuestion.data['post'])
        likeAdd = int(serializerQuestion.data['count'])
        data = Like.objects.filter(post=postId)
        if data:
            old = int(data['count'])
            Like.objects.filter(post=postId).update(count=likeAdd+old)
            return Response({'result': 'Updated'})
        else:
            b = Like.objects.create(count=likeAdd, post=postId)
            return Response({'result': 'Created'})




        return Response({'result':data})
        # return Response({'result':serializerQuestion.data['post']})



