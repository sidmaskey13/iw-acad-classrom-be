from rest_framework.response import Response

from all_apps.models import Post

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from all_apps.serializers.post import PostSerializer
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PostPaginate(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all().order_by('-id')
    pagination_class = PostPaginate
    page_size = 3

    @method_decorator(cache_page(60 * 5))
    def list(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        serializer = PostSerializer(instance=self.get_object())
        if self.request.user.id == serializer.data['user']:
            self.get_object().delete()
            return Response({'status': 'OK', 'message': 'Item deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
