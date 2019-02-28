from urllib.parse import parse_qs

import graphene
from graphql import ResolveInfo, GraphQLError

from apps.for_django.models import User as DBUser
from utils import jwt_auth
from utils.oauth import facebook
from utils.oauth.facebook import oauth


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


class SocialAuthCallbackInput(graphene.InputObjectType):
    session = graphene.String()
    provider = graphene.String(required=True)
    response = graphene.String(required=True)
    clientMutationId = graphene.String()


class SocialAuthCallbackPayload(graphene.Mutation):
    class Arguments:
        input = SocialAuthCallbackInput(required=True)

    token = graphene.String()
    refreshToken = graphene.String()
    clientMutationId = graphene.String()

    def mutate(self, info: ResolveInfo, input: SocialAuthCallbackInput):
        provider = input.provider
        response = input.response
        if provider == 'facebook':
            code = parse_qs(response)['code'][0]
            tokens = facebook.oauth(code)
            if tokens:
                print(tokens)  # save it
                token = tokens['access_token']
                user_detail = facebook.get_user_detail(token)
                print(user_detail)
                encoded = jwt_auth.encode(1)
                return SocialAuthCallbackPayload(
                    token=encoded,
                    refreshToken='refreshToken',
                    clientMutationId='clientMutationId'
                )
        return SocialAuthCallbackPayload(
            token='none',
            refreshToken='refreshToken',
            clientMutationId='clientMutationId'
        )


class UserMutation(graphene.ObjectType):
    login = Token.Field()
    social_auth_callback = SocialAuthCallbackPayload.Field()
