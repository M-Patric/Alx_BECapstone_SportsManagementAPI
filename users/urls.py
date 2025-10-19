from django.urls import path
from rest_framework.authtoken import views as drf_views
from .views import RegisterView, CustomObtainAuthToken, MeView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomObtainAuthToken.as_view(), name="login"),
    path("me/", MeView.as_view(), name="me"),
]
