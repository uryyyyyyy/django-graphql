from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('user/', include("apps.django_user.urls")),
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
