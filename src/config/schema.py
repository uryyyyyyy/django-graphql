import graphene

from apps.for_django.graphql_mutation import UserMutation
from apps.for_django.graphql_query import UserQuery


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
