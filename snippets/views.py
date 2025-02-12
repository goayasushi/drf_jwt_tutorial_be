from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)
