import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

User = get_user_model()


class PostCreateTestCase(APITestCase):
    def test_create(self):
        data = {"title": "Potman testing","body": "I am sam and i studied in acem"}
        response = self.client.post("api/post",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class PostViewTestCase(APITestCase):
    def test_create(self):
        response = self.client.post("api/post")
        self.assertEqual(response.status_code,status.HTTP_100_CONTINUE)