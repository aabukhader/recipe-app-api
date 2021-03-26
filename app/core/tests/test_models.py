from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_suc(self):
        # create new user with an email is successfuly
        email = 'abdallah.abukhader@abwaab.me'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the email for new user is normalized
        email = 'test@AbwaaB.me'
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test if user email valid
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_user_is_created(self):
        # Test creating a new superuser
        user = get_user_model().objects.create_superuser(
            'admin@admin.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
