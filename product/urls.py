from django.urls   import path
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1f08d08 (UPDATE: productdetail View, test complete.)
from product.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
<<<<<<< HEAD
=======
=======
from product.views import ProductDetailView

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
>>>>>>> 00dd63f (UPDATE: productdetail View, test complete.)
>>>>>>> 1f08d08 (UPDATE: productdetail View, test complete.)

]
