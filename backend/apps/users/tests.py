from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        """
        Ensure we can register a new user.
        """
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123",
        }
        response = self.client.post("/api/auth/register", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")
        self.assertTrue(User.objects.get().check_password("testpassword123"))

    def test_login_user(self):
        """
        Ensure we can log in a user and get an access token.
        """
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )
        data = {"email": "testuser@example.com", "password": "testpassword123"}
        response = self.client.post("/api/auth/login", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.data)