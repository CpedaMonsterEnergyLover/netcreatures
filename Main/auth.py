import requests
from functools import wraps
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


def extract_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise AuthenticationFailed('Authorization header missing or invalid.')

    token = auth_header.split(' ')[1]

    return token


def get_token_email(token):
    response = requests.get(f'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token}')

    if response.status_code != 200:
        raise AuthenticationFailed('Invalid token')

    user_data = response.json()
    email = user_data.get('email')
    if not email:
        raise AuthenticationFailed('Invalid token data')

    return email


def only_authenticated(view_func):

    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        token = extract_token(request)
        email = get_token_email(token)

        try:
            user = User.objects.get(email=email)
            request.user = user
            return view_func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

    return _wrapped_view
