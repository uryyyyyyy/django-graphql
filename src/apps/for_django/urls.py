from django.urls import path

from apps.for_django.view import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]
