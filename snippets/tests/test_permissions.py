from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly


class TestIsOwnerOrReadOnly(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="password123")
        self.other_user = User.objects.create_user(
            username="otherUser", password="password123"
        )
        self.snippet = Snippet.objects.create(
            title="test snippet", code="print(hello)", owner=self.owner
        )
        self.permission = IsOwnerOrReadOnly()
        self.factory = APIRequestFactory()

    def test_get_request_allow_anyone(self):
        request = self.factory.get("/")
        request.user = self.other_user
        self.assertTrue(
            self.permission.has_object_permission(request, None, self.snippet)
        )

    def test_owner_can_edit(self):
        request = self.factory.put("/")
        request.user = self.owner
        self.assertTrue(
            self.permission.has_object_permission(request, None, self.snippet)
        )

    def test_other_user_cannot_edit(self):
        request = self.factory.put("/")
        request.user = self.other_user
        self.assertFalse(
            self.permission.has_object_permission(request, None, self.snippet)
        )

    def test_anonymous_user_cannot_edit(self):
        request = self.factory.put("/")
        request.user = None
        self.assertFalse(
            self.permission.has_object_permission(request, None, self.snippet)
        )
