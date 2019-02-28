from typing import Optional

from apps.for_django.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.deprecation import MiddlewareMixin

from utils.jwt import decode


def get_user(user_id) -> Optional[User]:
    try:
        return User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return None


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is not None:
            user_id = decode(token)
            if user_id is not None:
                user = get_user(user_id)
                if user is not None:
                    request.user = user
