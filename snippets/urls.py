from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"", views.SnippetViewSet, basename="snippet")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
