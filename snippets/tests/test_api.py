from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from snippets.models import Snippet


class TestSnippetAPI(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="password123")
        self.other_user = User.objects.create_user(
            username="otherUser", password="password123"
        )
        self.snippet = Snippet.objects.create(
            title="test snippet",
            code="print(hello)",
            linenos=True,
            language="python",
            owner=self.owner,
        )

    def test_query_snippet_list_without_auth(self):
        """
        認証なしでもスニペット一覧を取得できる
        """
        url = reverse("snippet-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_query_snippet_detail_without_auth(self):
        """
        認証なしで個別スニペットの詳細が取得できる
        """
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.snippet.id)
        self.assertEqual(response.data["title"], self.snippet.title)

    def test_post_snippet_authenticated(self):
        """
        認証済みユーザーはスニペットを作成できる（owner が自動設定される）
        """
        self.client.force_authenticate(user=self.owner)
        url = reverse("snippet-list")
        input_data = {
            "title": "new snippet",
            "code": "print(new code)",
            "linenos": True,
            "language": "python",
        }

        response = self.client.post(url, input_data)
        self.assertEqual(response.status_code, 201)
        new_snippet = Snippet.objects.get(title="new snippet")
        self.assertEqual(new_snippet.owner, self.owner)

    def test_post_snippet_without_auth(self):
        """
        未認証ユーザーはスニペットの作成ができない
        """
        url = reverse("snippet-list")
        input_data = {
            "title": "new snippet",
            "code": "print(new code)",
            "linenos": True,
            "language": "python",
        }

        response = self.client.post(url, input_data)
        self.assertEqual(response.status_code, 401)

    def test_put_snippet_as_owner(self):
        """
        所有者はスニペットを更新できる
        """
        self.client.force_authenticate(user=self.owner)
        url = reverse("snippet-detail", args=[self.snippet.pk])
        input_data = {
            "title": "Updated Snippet",
            "code": "print('Updated Code')",
            "linenos": False,
            "language": "python",
        }
        response = self.client.put(url, input_data)
        self.assertEqual(response.status_code, 200)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, "Updated Snippet")

    def test_put_snippet_as_non_owner(self):
        """
        所有者以外はスニペットを更新できない
        """
        self.client.force_authenticate(user=self.other_user)
        url = reverse("snippet-detail", args=[self.snippet.pk])
        input_data = {
            "title": "Updated Snippet",
            "code": "print('Updated Code')",
            "linenos": False,
            "language": "python",
        }
        response = self.client.put(url, input_data)
        self.assertEqual(response.status_code, 403)

    def test_put_snippet_without_auth(self):
        """
        未認証ユーザーはスニペットを更新できない
        """
        url = reverse("snippet-detail", args=[self.snippet.pk])
        input_data = {
            "title": "Updated Snippet",
            "code": "print('Updated Code')",
            "linenos": False,
            "language": "python",
        }
        response = self.client.put(url, input_data)
        self.assertEqual(response.status_code, 401)

    def test_delete_snippet_as_owner(self):
        """
        所有者はスニペットを削除できる
        """
        self.client.force_authenticate(user=self.owner)
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Snippet.DoesNotExist):
            Snippet.objects.get(pk=self.snippet.pk)

    def test_delete_snippet_as_non_owner(self):
        """
        所有者以外はスニペットを削除できない
        """
        self.client.force_authenticate(user=self.other_user)
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

    def test_delete_snippet_without_auth(self):
        """
        未認証ユーザーはスニペットを削除できない
        """
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)
