import json
from django.db import reset_queries

from django.http            import JsonResponse, HttpResponse
from django.views           import View
from django.db.models       import Q, Count

from user.utils     import login_decorator, login_check
from .models import Brand, Category, Product, ProductUserlike, Review

class ProductListView(View):
    @login_check
    def get(self, request):
        user          = request.user

        category_list = request.GET.getlist('category', None)
        sort          = request.GET.get('sort', 'latestOrder')
        
        q = Q()
        if category_list:
            for category in category_list:
                q.add(Q(category=category), q.OR)

        sort_dict = {
                'latestOrder'     : '-created_at',
                'reviewCountOrder': '-num_reviews',
                'popularOrder'    : '-like_product'
        }

        if sort in sort_dict:
            products = Product.objects.filter(q)\
                    .annotate(num_reviews=Count('review')).order_by(sort_dict[sort])
        
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
                
class ProductDetailView(View):
    @non_user_accept_decorator
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        user = request.user
        like     = ProductUserlike.objects.filter(user_id=user.id, product_id=product.id).exists() if user else False
        product_info_list = [{
            "id"          : product.id,
            "thumbnail"   : product.thumbnail_url,
            "likeCount"   : ProductUserlike.objects.filter(product_id=product.id).count(),
            "like"        : like,
            "category"    : product.category.name,
            "creatorName" : product.user.name,
            "className"   : product.title,
            "price"       : product.price,
	    "gift"        : product.gift,
            "description" : product.description,
            "introduction": product.introduction,
            "reviews"     : [{ 
                "id"      : review.id,
                "author"  : review.user.name,
                "text"    : review.description
            }for review in Review.objects.filter(product_id=product.id)]
        }]

        return JsonResponse({"product": product_info_list}, status=200)


