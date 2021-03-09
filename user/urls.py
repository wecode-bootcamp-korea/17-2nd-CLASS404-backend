from django.urls import path
from .views      import KakaoLoginView, MyPageView

urlpatterns = [
    path('/kakaologin', KakaoLoginView.as_view()),
    path('/mypage', MyPageView.as_view()),
]