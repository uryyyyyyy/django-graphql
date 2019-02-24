from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include("apps.django_user.urls")),
    path('admin/', admin.site.urls),
]
