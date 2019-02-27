import graphene
from graphql import ResolveInfo
from apps.for_django.models import User as DBUser
from utils.choices import USER_ROLES
from utils.graphql_auth import login_required_resolver, permission_required_resolver


class User(graphene.ObjectType):
    email = graphene.String()
    name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info: ResolveInfo):
        return f'{self.email} - {self.name}'


class UserQuery(graphene.ObjectType):
    allUsers = graphene.List(User, pk_gte=graphene.Boolean())
    user = graphene.Field(User, pk=graphene.Int())

    @login_required_resolver
    def resolve_allUsers(self, info: ResolveInfo, pk_gte: bool):
        if pk_gte:
            return [User(email=user.email, name=user.name) for user in DBUser.objects.order_by('-id')]
        return [User(email=user.email, name=user.name) for user in DBUser.objects.all()]

    @permission_required_resolver(USER_ROLES.ADMINISTRATOR)
    def resolve_user(self, info: ResolveInfo, pk):
        print(pk)
        user = DBUser.objects.get(pk=pk)
        return User(email=user.email, name=user.name)
