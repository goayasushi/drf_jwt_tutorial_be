from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class TestSnippetSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.snippet = Snippet.objects.create(
            title="test snippet",
            code="print(hello)",
            linenos=True,
            language="python",
            owner=self.user,
        )
        self.factory = APIRequestFactory()
        self.request = self.factory.get("/")
        self.context = {"request": Request(self.request)}

    def test_snippet_serializer_output(self):
        serializer = SnippetSerializer(instance=self.snippet, context=self.context)
        data = serializer.data

        # urlを動的に取得する
        expected_url = reverse(
            "snippet-detail", args=[self.snippet.pk], request=self.request
        )
        expected_data = {
            "url": expected_url,
            "id": self.snippet.id,
            "title": self.snippet.title,
            "code": self.snippet.code,
            "linenos": self.snippet.linenos,
            "language": self.snippet.language,
            "owner": self.user.username,
        }

        self.assertEqual(data, expected_data)

    def test_snippet_serializer_input_valid(self):
        """
        入力データのバリデーション(ok)
        """

        input_data = {
            "title": "test snippet",
            "code": "print(hello)",
            "linenos": True,
            "language": "python",
        }

        serializer = SnippetSerializer(data=input_data, context=self.context)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_snippet_serializer_input_valid_code_without(self):
        """
        入力データのバリデーション(ng: codeが存在しない)
        """

        input_data = {
            "title": "test snippet",
            "linenos": True,
            "language": "python",
        }

        serializer = SnippetSerializer(data=input_data, context=self.context)
        self.assertFalse(serializer.is_valid())
        self.assertIn("code", serializer.errors)

    def test_snippet_serializer_input_valid_code_blank(self):
        """
        入力データのバリデーション(ng: codeが空文字)
        """

        input_data = {
            "title": "test snippet",
            "code": "",
            "linenos": True,
            "language": "python",
        }

        serializer = SnippetSerializer(data=input_data, context=self.context)
        self.assertFalse(serializer.is_valid())
        self.assertIn("code", serializer.errors)

    def test_snippet_serializer_input_valid_code_None(self):
        """
        入力データのバリデーション(ng: codeがNone)
        """

        input_data = {
            "title": "test snippet",
            "code": None,
            "linenos": True,
            "language": "python",
        }

        serializer = SnippetSerializer(data=input_data, context=self.context)
        self.assertFalse(serializer.is_valid())
        self.assertIn("code", serializer.errors)
