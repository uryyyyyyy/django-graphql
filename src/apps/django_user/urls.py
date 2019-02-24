from django.urls import path

from apps.django_user.view import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]
