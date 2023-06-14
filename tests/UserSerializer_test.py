import yaml
# from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth.models import User
from serializers import UserSerializer

class UserSerializerTest(TestCase):

    def setUp(self):
        with open('fixtures/users.yaml') as file:
            self.fixture_data = yaml.load(file, Loader=yaml.FullLoader)

    def test_user_serializer_valid_user(self):
        valid_user_data = self.fixture_data['valid_user']
        
        serializer = UserSerializer(data=valid_user_data)

        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, valid_user_data['email'])
        self.assertEqual(user.first_name, valid_user_data['first_name'])
        self.assertEqual(user.last_name, valid_user_data['last_name'])
        serializer = UserSerializer(data=valid_user_data)

        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, valid_user_data['email'])
        self.assertEqual(user.first_name, valid_user_data['first_name'])
        self.assertEqual(user.last_name, valid_user_data['last_name'])

    def test_user_serializer_invalid_user_missing_email(self):
        invalid_user_data = self.fixture_data['invalid_user_missing_email']
        serializer = UserSerializer(data=invalid_user_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_user_serializer_invalid_user_missing_first_name(self):
        invalid_user_data = self.fixture_data['invalid_user_missing_first_name']
        serializer = UserSerializer(data=invalid_user_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('first_name', serializer.errors)

    def test_user_serializer_invalid_user_missing_last_name(self):
        invalid_user_data = self.fixture_data['invalid_user_missing_last_name']
        serializer = UserSerializer(data=invalid_user_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('last_name', serializer.errors)