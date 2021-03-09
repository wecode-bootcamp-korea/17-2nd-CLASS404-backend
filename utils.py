import jwt
import json

from django.http    import JsonResponse

from my_settings    import SECRET_KEY, ALGORITHM
from user.models    import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        print('hello')
        if 'Authorization' not in request.headers:
            return JsonResponse({'MESSAGE': 'NEED_LOGIN'}, status=401)
        try:
            access_token = request.headers['Authorization']
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            login_user   = User.objects.get(id=payload['user_id'])
            request.user = login_user
            return func(self, request, *args, **kwargs)
        except jwt.DecodeError:
            return JsonResponse({'MESSAGE': 'INVALID_TOKEN'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)
    return wrapper
