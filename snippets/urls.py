from django.urls import path
from snippets import views

urlpatterns = [
    path("", views.SnippetList.as_view(), name="snippet-list"),
    path("<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
]
