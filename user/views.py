import json
import bcrypt
import jwt
import requests
import re

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from my_settings    import SECRET_KEY, ALGORITHM
from user.utils     import login_decorator
from .models        import User, UserType, UserTier
from product.models import Brand, Category, Product, ProductUserlike, Review

USER_TIER_DEFAULT_ID = 1
USER_TYPE_DEFAULT_ID = 1

class SignupView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']                                
            name     = data['name']
            password_regex = re.compile("(?=.*\d)(?=.*[a-z]).{8,32}$", re.IGNORECASE)
            if not password_regex.match(password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            email_regex = re.compile("^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$")
            if not email_regex.match(email):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)

            if not name:
                return JsonResponse({'message' : 'INVALID_NAME'}, status = 400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'DUPLICATED_EMAIL'}, status = 400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email        = email,
                password     = hashed_password,
                name         = name,
                tier_id      = USER_TIER_DEFALUT_ID,
                user_type_id = USER_TYPE_DEFALUT_ID
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
                
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

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

class MyPageView(View):
    @login_decorator
    def get(self, request):
        user = request.user

        class_type = request.GET.get('class', 'like')
        class_dict = {
            'like'  : Q(productuserlike__user=user),
            'buy'   : Q(order__user=user),
            'create': Q(user=user),
        }

        q = Q(class_dict[class_type])

        products = Product.objects.filter(q).order_by('-created_at')
        
        product_info_list = [{
            "id"          : product.id,
            "thumbnail"   : product.thumbnail_url,
            "likeCount"   : ProductUserlike.objects.filter(product_id=product.id).count(), 
            "like"        : ProductUserlike.objects.filter(user_id=user.id, product_id=product.id).exists() if user else False,
            "category"    : product.category.name,
            "userName"    : product.user.name,
            "title"       : product.title,
            "price"       : product.price,
	        "gift"        : product.gift,
        } for product in products]
        return JsonResponse({"product": product_info_list}, status=200)

class SigninView(View):
    def post(self, request):
        try: 
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            user = User.objects.get(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'user_id': user.id}, SECRET_KEY, ALGORITHM)
                return JsonResponse({'message': 'SUCCESS', 'access_token': token}, status=200)
            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
