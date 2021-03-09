import json
from os import access
import jwt
import bcrypt

from django.test     import TestCase, Client

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

from user.models     import (
        UserTier,
        UserType,
        User
        )
from my_settings     import SECRET_KEY, ALGORITHM
from user.utils      import login_decorator

TestCase.maxDiff = None

USER_TIER_DEFAULT_ID = 1
USER_TYPE_DEFAULT_ID = 1

class ProductDetailTest(TestCase):
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

        ProductUserlike.objects.create(id=1, product_id=2, user_id=1)

        Review.objects.create(id=1, user_id=1, product_id=1, description="this is 1st test description.")
        
        Review.objects.create(id=2, user_id=2, product_id=1, description="this is 2nd test description")


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

    def test_productview_user_get_success(self):
        client   = Client()
        response = client.get("/product", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'product': [{'id': 2, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 1, 'like': True, 'category': '음악', 'userName': '데이비드', 'title': '원피스', 'price': '50000.00', 'gift': False}, {'id': 1, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 0, 'like': False, 'category': '미술', 'userName': '이동근', 'title': '아따맘마', 'price': '50000.00', 'gift': False}]})
    
    def test_productview_non_user_get_success(self):
        client   = Client()
        response = client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'product': [{'id': 2, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 1, 'like': False, 'category': '음악', 'userName': '데이비드', 'title': '원피스', 'price': '50000.00', 'gift': False}, {'id': 1, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 0, 'like': False, 'category': '미술', 'userName': '이동근', 'title': '아따맘마', 'price': '50000.00', 'gift': False}]})
    
    def test_productview_get_not_found(self):
        client   = Client()
        response = client.get('/products')
        Review.objects.all().delete()

    def test_productdetailview_user_get_success(self):
        client   = Client()
        response = client.get("/product/1", **{"HTTP_AUTHORIZATION":self.access_token,"content_type" : "application/json"})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'product': [{'id': 1, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 0, 'like': False, 'category': '미술', 'creatorName': '이동근', 'className': '아따맘마', 'price': '50000.00', 'gift': False, 'description': '', 'introduction': '안녕하세요', 'reviews': [{'id': 1, 'author': '이동근', 'text': 'this is 1st test description.'}, {'id': 2, 'author': '데이비드', 'text': 'this is 2nd test description'}]}]})

    def test_productdetailview_non_user_get_success(self):
        client = Client()
        response = client.get("/product/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'product': [{'id': 2, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 1, 'like': False, 'category': '음악', 'userName': '데이비드', 'title': '원피스', 'price': '50000.00', 'gift': False},'review':[{"id":1, "author":'이동근', "text":           "this is 1st test description"}], {'id': 1, 'thumbnail': 'https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', 'likeCount': 0, 'like': False, 'category': '미술', 'userName': '이동근', 'title': '아따맘마', 'price': '50000.00', 'gift': False, 'review':[{"id":1, "author":'이동근', "text":           "this is 1st test description"}]}]})
    
    def test_productview_get_not_found(self):
        client   = Client()
        response = client.get('/product/productdetail')
        self.assertEqual(response.status_code, 404)
    

    
