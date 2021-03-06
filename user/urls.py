from django.urls import path
from .views      import KakaoLoginView, MyPageView, SigninView, SignupView, MyPageView, MyPageImageUploadView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/kakaologin', KakaoLoginView.as_view()),
    path('/mypage', MyPageView.as_view()),
    path('/mypage/image', MyPageImageUploadView.as_view()),
    path('/signin', SigninView.as_view())
]
