from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
from django.utils.deprecation import MiddlewareMixin

import os
from datetime import datetime, timedelta

import jwt
from jwt import DecodeError

UserModel = get_user_model()

PRIVATE_KEY = os.environ['JWT_PRIVATE_KEY'].replace("\\n", "\n")
PUBLIC_KEY = os.environ['JWT_PUBLIC_KEY'].replace("\\n", "\n")
EXPIRATION_DELTA = timedelta(days=14)


def encode(user_id: int)-> str:
    return jwt.encode(
        {'user_id': user_id, 'exp': datetime.utcnow() + EXPIRATION_DELTA},
        PRIVATE_KEY,
        algorithm='RS256'
    ).decode("utf-8")


def decode(token: str)-> int:
    try:
        return jwt.decode(str.encode(token), PUBLIC_KEY, algorithms='RS256')['user_id']
    except DecodeError:
        return None


def get_user(user_id):
    try:
        return UserModel._default_manager.get(pk=user_id)
    except UserModel.DoesNotExist:
        return None


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request: WSGIRequest):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is not None:
            user_id = decode(token)
            if user_id is not None:
                user = get_user(user_id)
                if user is not None:
                    request.user = user
