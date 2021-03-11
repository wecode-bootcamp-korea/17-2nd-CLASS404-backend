from django.urls   import path
from product.views import ProductView, ProductDetailView, FileView


urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path("/file", FileView.as_view()),

]
