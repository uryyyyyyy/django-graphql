from typing import List

from graphql import ResolveInfo, GraphQLError

from utils.choices import USER_ROLES


def login_required_resolver(f):
    def wrapper(self, info: ResolveInfo, *args, **kwargs):
        if info.context.user.is_authenticated:
            return f(self, info, *args, **kwargs)
        else:
            raise GraphQLError("LOGIN_REQUIRED")
    return wrapper


def permission_required_resolver(roles: List[str]):
    def wrap(f):
        def wrapped_f(self, info: ResolveInfo, *args, **kwargs):
            if not info.context.user.is_authenticated:
                raise GraphQLError("LOGIN_REQUIRED")
            if info.context.user.role in roles:
                return f(self, info, *args, **kwargs)
            else:
                raise GraphQLError("PERMISSION_DENIED")
        return wrapped_f
    return wrap
