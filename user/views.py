import json
import bcrypt
import jwt
import requests

from django.views import View
from django.http  import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from .models      import User, UserType, UserTier

USER_TIER_DEFAULT_ID = 1
USER_TYPE_DEFAULT_ID = 1

class KakaoLoginView(View):
    def get(self, request):
        try:
            access_token = request.headers["Authorization"]
            headers      =({'Authorization' : f"Bearer {access_token}"})
            url          = "https://kapi.kakao.com/v2/user/me"
            response     = requests.post(url, headers=headers)
            user         = response.json()

            if user.get('msg', None):
                return JsonResponse({'message':'INVALID_TOKEN'}, status = 400)

            name  = user['properties']['nickname']
            email = user['kakao_account'].get('email')

            if User.objects.filter(social_login = user['id']).exists():
                user_info   = User.objects.get(social_login=user['id'])
                token = jwt.encode({'user_id': user_info.id}, SECRET_KEY, ALGORITHM)

                return JsonResponse({
                    'access_token': token,
                    'user_name': name,
                    'message': "SUCCESS"
                    }, status=200)
                    
            user_info = User(
                social_login = user['id'],
                name         = name,
                email        = email,
                tier_id      = USER_TIER_DEFAULT_ID,
                user_type_id = USER_TYPE_DEFAULT_ID
            )
            user_info.save()
            token = jwt.encode({'user_id': user_info.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({
                'access_token': token,
                'user_name': name,
                'message': "SUCCESS"
                }, status=201)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)     