from django.urls import path
from .views      import KakaoLoginView

urlpatterns = [
    path('/kakaologin', KakaoLoginView.as_view()),
]