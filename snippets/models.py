from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # 作成日時（自動設定）
    title = models.CharField(max_length=100, blank=True, default="")  # タイトル（任意）
    code = models.TextField()  # コードスニペット本体
    linenos = models.BooleanField(default=False)  # 行番号を表示するかどうか
    language = models.CharField(default="python", max_length=100)  # プログラミング言語
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]  # 作成日時で並び替え
