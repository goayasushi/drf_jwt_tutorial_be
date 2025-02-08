from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views

urlpatterns = [
    path("auth/jwt", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth-user/", views.CurrentUserView.as_view(), name="current-user"),
    path("register/", views.UserRegistrationView.as_view(), name="user-register"),
]
