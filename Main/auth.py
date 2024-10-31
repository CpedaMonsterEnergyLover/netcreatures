import requests
from functools import wraps
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


def only_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('Authorization header missing or invalid.')

        token = auth_header.split(' ')[1]

        # Verify token with Google
        response = requests.get(f'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token}')
        print(token)
        print(response.json())


        if response.status_code != 200:
            raise AuthenticationFailed('Invalid token')

        user_data = response.json()
        email = user_data.get('email')
        if not email:
            raise AuthenticationFailed('Invalid token')

        user = User.objects.get(email=email)

        if not user:
            raise AuthenticationFailed('Invalid token')

        request.user = user
        return view_func(self, request, *args, **kwargs)

    return _wrapped_view
