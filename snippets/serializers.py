from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet  # 使用するモデルを指定
        fields = ["id", "title", "code", "linenos", "language", "owner"]
