from django.urls import path
from .views      import KakaoLoginView, SignupView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/kakaologin', KakaoLoginView.as_view()),
]