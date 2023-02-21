"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests models."""

    def test_create_user_with_email_succesful(self):
        """"Test create an user with email is succesfull"""
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))