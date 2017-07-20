from accounts.models import Token
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTestCase(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email='x@y.com')
        self.assertEqual(user.pk, 'x@y.com')

class TokenModelTestCase(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='x@y.com')
        token2 = Token.objects.create(email='x@y.com')
        self.assertNotEqual(token1.uid, token2.uid)
