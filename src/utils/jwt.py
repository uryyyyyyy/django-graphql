from typing import Optional

import os
from datetime import datetime, timedelta

import jwt
from jwt import DecodeError

PRIVATE_KEY = os.environ['JWT_PRIVATE_KEY'].replace("\\n", "\n")
PUBLIC_KEY = os.environ['JWT_PUBLIC_KEY'].replace("\\n", "\n")
EXPIRATION_DELTA = timedelta(days=14)


def encode(user_id: int)-> str:
    return jwt.encode(
        {'user_id': user_id, 'exp': datetime.utcnow() + EXPIRATION_DELTA},
        PRIVATE_KEY,
        algorithm='RS256'
    ).decode("utf-8")


def decode(token: str)-> Optional[int]:
    try:
        return jwt.decode(str.encode(token), PUBLIC_KEY, algorithms='RS256')['user_id']
    except DecodeError:
        return None
