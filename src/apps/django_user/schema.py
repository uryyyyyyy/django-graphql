import graphene
from graphql import ResolveInfo


class User(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info: ResolveInfo):
        return f'{self.first_name} - {self.last_name}'


class UserQuery(graphene.ObjectType):
    allUsers = graphene.List(User, pk_gte=graphene.Boolean())
    user = graphene.Field(User, pk=graphene.Int())

    def resolve_allUsers(self, info: ResolveInfo, pk_gte: bool):
        print(pk_gte)
        user1 = User(first_name="first", last_name="last")
        user2 = User(first_name="222", last_name="last_222")
        return [user1, user2]

    def resolve_user(self, info: ResolveInfo, pk):
        print(pk)
        return User(first_name="first", last_name="last")


schema = graphene.Schema(query=UserQuery)
