from django.urls import path
from snippets import views

urlpatterns = [
    path("", views.SnippetList.as_view()),
    path("<int:pk>/", views.SnippetDetail.as_view()),
]
