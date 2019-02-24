from django.urls import path, include

urlpatterns = [
    path('user/', include("apps.django_user.urls")),
]
