import graphene
from graphql import ResolveInfo, GraphQLError

from apps.for_django.models import User as DBUser
from utils import jwt_auth


class Token(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user_id = graphene.Int()
    token = graphene.String()

    def mutate(self, info: ResolveInfo, email: str, password: str):
        print(info.context.user)
        user: DBUser = DBUser.objects.get(email=email)
        if not user.check_password(password):
            raise GraphQLError('LOGIN_FAILED')
        encoded = jwt_auth.encode(user.id)
        return Token(user_id=user.id, token=encoded)


class UserMutation(graphene.ObjectType):
    login = Token.Field()
