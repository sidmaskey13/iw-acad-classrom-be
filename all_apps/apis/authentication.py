from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import generics,permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import get_user_model

from all_apps.models import UserDetail
from all_apps.serializers.authentication import UserSerializer, RegisterSerializer, LoginSerializer, \
    RegisterStaffSerializer, AllUserSerializer
User = get_user_model()


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if request.FILES['profile_pic']:
            myfile = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            profile = UserDetail()
            profile.user = user
            profile.profile_pic = uploaded_file_url
            profile.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class RegisterStaffAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if request.FILES['profile_pic']:
            myfile = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            profile = UserDetail()
            profile.user = user
            profile.profile_pic = uploaded_file_url
            profile.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class AllUserAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = AllUserSerializer
    queryset = User.objects.all()


class UserDeleteAPI(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsAdminUser,]
    serializer_class = AllUserSerializer

    queryset = User.objects.all()
