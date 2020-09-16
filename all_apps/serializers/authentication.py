from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from all_apps.models import UserDetail


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'is_superuser')


class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile_pic = ProfilePicSerializer(source='user_detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email','profile_pic','is_staff','is_superuser')


class RegisterSerializer(serializers.ModelSerializer):
    profile_pic = ProfilePicSerializer(source='user_detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'profile_pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # is_staff=True
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credintials')


class RegisterStaffSerializer(serializers.ModelSerializer):
    profile_pic = ProfilePicSerializer(source='user_detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'profile_pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # is_staff=True
        )
        return user



