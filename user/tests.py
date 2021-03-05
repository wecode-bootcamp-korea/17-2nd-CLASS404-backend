import json
import bcrypt

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock
from requests.auth import HTTPBasicAuth

from .models import User, UserType, UserTier

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
    