import os
from typing import Optional

import requests
from requests import Response

OAUTH2_ID = os.environ['OAUTH2_FACEBOOK_ID']
OAUTH2_SECRET = os.environ['OAUTH2_FACEBOOK_SECRET']
OAUTH2_REDIRECT = os.environ['OAUTH2_FACEBOOK_REDIRECT']


def oauth(code: str)-> Optional[dict]:
    url = f'https://graph.facebook.com/v3.2/oauth/access_token?client_id={OAUTH2_ID}' \
        f'&redirect_uri={OAUTH2_REDIRECT}&client_secret={OAUTH2_SECRET}&code={code}'
    response: Response = requests.get(url)
    if response.status_code != 200:
        print(response.json())
        return None
    return response.json()


def get_user_detail(token: str) -> Optional[dict]:
    url = f'https://graph.facebook.com/v3.2/me?access_token={token}&fields=id,email'
    response: Response = requests.get(url)
    if response.status_code != 200:
        print(response.json())
        return None
    return response.json()
