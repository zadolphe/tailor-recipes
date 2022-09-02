"""
Tests models
"""

from multiprocessing.sharedctypes import Value
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for model user"""

    """first test if create user email was successful"""
    def test_create_user_email(self, ):
        email = "test@example.com"
        password = "testpassword1"
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )


        self.assertEqual(user.email, email)
        """We use the check_password method here bc we will have a hash value of the pass stored
        so this method checks that by seeing of it is the same hash"""
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.Com', 'TEST3@example.com'],
            ['test4@example.Com', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a valueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass1')

    def test_create_superuser(self):
        """test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)