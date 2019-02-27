import graphene

from apps.django_user.schema import UserQuery


class Query(UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
