from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path, include
from graphene_django.views import GraphQLView


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


urlpatterns = [
    path('user/', include("apps.for_django.urls")),
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
