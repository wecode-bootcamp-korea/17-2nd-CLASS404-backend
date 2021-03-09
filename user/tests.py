import json
import jwt
import bcrypt

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock
from requests.auth import HTTPBasicAuth

from product.models  import (
    Brand,
    Category,
    Gender,
    ClassLevel,
    ProductImage,
    Age,
    Product,
    ProductAge,
    ProductUserlike,
    Review
    )

from user.models  import UserTier, UserType, User
from order.models import Order, Address, OrderStatus

from my_settings     import SECRET_KEY, ALGORITHM
from user.utils      import login_decorator

TestCase.maxDiff = None

USER_TIER_DEFAULT_ID = 1
USER_TYPE_DEFAULT_ID = 1

class KakaoLoginTest(TestCase):
    def setUp(self):
        UserTier.objects.create(id=1, name="브론즈")
        UserType.objects.create(id=1, name="일반")
        User.objects.create(
            social_login = '67890',
            name         = "이준하",
            email        = "dlwnsgk@gmail.com",
            tier_id      = USER_TIER_DEFAULT_ID,
            user_type_id = USER_TYPE_DEFAULT_ID
        )

    def tearDown(self):
        UserTier.objects.all().delete()
        UserType.objects.all().delete()
        User.objects.all().delete()

    @patch("user.views.requests")
    def test_kakaosignupview_get_success(self, mocked_requests):
        client   = Client()
        
        class MockedResponse:
            def json(self):
                return {
                    "id" : "12345",
                    "properties" : {
                        "nickname" : "박재현"
                    },
                    "kakao_account":{
                        "email":"namujinju@gmail.com"
                    }
                }
                
        mocked_requests.post = MagicMock(return_value = MockedResponse())
        
        response = client.get("/user/kakaologin", **{"HTTP_AUTHORIZATION":"1234","content_type" : "application/json"})
        self.assertEqual(response.status_code, 201)
    
    @patch("user.views.requests")
    def test_kakaologinview_get_success(self, mocked_requests):
        client   = Client()
        
        class MockedResponse:
            def json(self):
                return {
                    "id" : "67890",
                    "properties" : {
                        "nickname" : "이준하"
                    },
                    "kakao_account":{
                        "email":"dlwnsgk@gmail.com"
                    }
                }

        mocked_requests.post = MagicMock(return_value = MockedResponse())
        
        response = client.get("/user/kakaologin", **{"HTTP_AUTHORIZATION":"1234","content_type" : "application/json"})
        self.assertEqual(response.status_code, 200)

    @patch("user.views.requests")
    def test_kakaologinview_get_fail(self, mocked_requests):
        client   = Client()

        class MockedResponse:
            def json(self):
                return {
                    'msg': 'this access token does not exist', 'code': -401
                }

        mocked_requests.post = MagicMock(return_value = MockedResponse())

        response = client.get("/user/kakaologin", **{"HTTP_AUTHORIZATION":"1234","content_type" : "application/json"})
        self.assertEqual(response.json(),{'message':'INVALID_TOKEN'})
        self.assertEqual(response.status_code, 400)
    
    def test_kakaologinview_get_not_found(self):
        client   = Client()
        response = client.get('/user/a')
        self.assertEqual(response.status_code, 404)

class MyPageTest(TestCase):
    def setUp(self):
        Brand.objects.create(id=1, name="취미")
        Category.objects.create(id=1, name="미술", brand_id=1)
        Category.objects.create(id=2, name="음악", brand_id=1)
        ClassLevel.objects.create(name='이동근')
        Age.objects.create(id=1, group='10대')
        UserTier.objects.create(id=1, name='브론즈')
        UserType.objects.create(id=1, name='일반')
        User.objects.create(
                id           =  1,
                social_login = '67890',
                name         = '이동근',
                email        = 'dlehdrms@gamil.com',
                tier_id      =  USER_TIER_DEFAULT_ID,
                user_type_id =  USER_TYPE_DEFAULT_ID
                )
        User.objects.create(
                id           =  2,
                social_login = '12345',
                name         = '데이비드',
                email        = 'david@gamil.com',
                tier_id      =  USER_TIER_DEFAULT_ID,
                user_type_id =  USER_TYPE_DEFAULT_ID
                )
                
        Product.objects.create(
                    id            = 1,
                    title         = "아따맘마",
                    price         = 50000.00,
                    gift          = False,
                    available_now = True,
                    introduction  = "안녕하세요",
                    thumbnail_url = "https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    user_id       = 1,
                    category_id   = 1,
                    satisfaction  = True,
                    )
        Product.objects.create(
                    id            = 2,
                    title         = "원피스",
                    price         = 50000.00,
                    gift          = False,
                    available_now = True,
                    introduction  = "반갑습니다.",
                    thumbnail_url = "https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    user_id       = 2,
                    category_id   = 2,
                    satisfaction  = False,
                    )
        Product.objects.create(
                    id            = 3,
                    title         = "나루토",
                    price         = 50000.00,
                    gift          = False,
                    available_now = True,
                    introduction  = "다시만나요",
                    thumbnail_url = "https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    user_id       = 1,
                    category_id   = 2,
                    satisfaction  = False,
                    )
        Product.objects.create(
                    id            = 4,
                    title         = "다다다",
                    price         = 50000.00,
                    gift          = True,
                    available_now = True,
                    introduction  = "잘가요",
                    thumbnail_url = "https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    user_id       = 2,
                    category_id   = 1,
                    satisfaction  = False,
                    )

        ProductUserlike.objects.create(id=1, product_id=2, user_id=1)

        Address.objects.create(id=1, name="서울 강남구 위워크 1호점")
        OrderStatus.objects.create(id=6, name="배송완료")
        Order.objects.create(
            total_cost = 50000,
            status_id  = 6,
            user_id    = 1,
            product_id = 4,
            address_id = 1
        )

        self.access_token = jwt.encode({'user_id' : User.objects.get(id=1).id},\
                SECRET_KEY, ALGORITHM)

    def tearDown(self):
        Product.objects.all().delete()
        ProductAge.objects.all().delete()
        Gender.objects.all().delete()
        ProductImage.objects.all().delete()
        ProductUserlike.objects.all().delete()
        Brand.objects.all().delete()
        Category.objects.all().delete()
        UserTier.objects.all().delete()
        UserType.objects.all().delete()
        User.objects.all().delete()
        Age.objects.all().delete()
        Address.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()

    def test_mypage_like_get_success(self):
        client = Client()
        response = client.get("/user/mypage?class=like", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product':
            [
                {
                    'id'        : 2,
                    'thumbnail' : 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                    'likeCount' : 1,
                    'like'      : True,
                    'category'  : '음악',
                    'userName'  : '데이비드',
                    'title'     : '원피스',
                    'price'     : '50000.00',
                    'gift'      : False
                }
            ]
        })
    
    def test_mypage_create_get_success(self):
        client = Client()
        response = client.get("/user/mypage?class=create", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product': 
            [
                {
                    'id': 3,
                    'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                    'likeCount': 0,
                    'like': False,
                    'category': '음악',
                    'userName': '이동근',
                    'title': '나루토',
                    'price': '50000.00',
                    'gift': False
                },
                {
                    'id': 1,
                    'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                    'likeCount': 0,
                    'like': False,
                    'category': '미술',
                    'userName': '이동근',
                    'title': '아따맘마',
                    'price': '50000.00',
                    'gift': False
                }
            ]
        })
    
    def test_mypage_buy_get_success(self):
        client = Client()
        response = client.get("/user/mypage?class=buy", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product':
            [
                {
                    'id': 4,
                    'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                    'likeCount': 0,
                    'like': False,
                    'category': '미술',
                    'userName': '데이비드',
                    'title': '다다다',
                    'price': '50000.00',
                    'gift': True
                }
            ]
        })

    def test_mypage_default_get_success(self):
        client = Client()
        response = client.get("/user/mypage", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product':
            [
                {
                    'id'        : 2,
                    'thumbnail' : 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                    'likeCount' : 1,
                    'like'      : True,
                    'category'  : '음악',
                    'userName'  : '데이비드',
                    'title'     : '원피스',
                    'price'     : '50000.00',
                    'gift'      : False
                }
            ]
        })

    def test_mypage_get_not_found(self):
        client   = Client()
        response = client.get('/a', **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        self.assertEqual(response.status_code, 404)

    
    

    

    