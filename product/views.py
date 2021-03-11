import json
from django.db import reset_queries

from django.http            import JsonResponse, HttpResponse
from django.views           import View
from django.db.models       import Q, Count

from user.utils     import login_decorator, login_check
from .models        import (
    Brand,
    Category, 
    Product, 
    ProductUserlike, 
    Review, 
    ProductImage,
    ClassLevel,
    Gender,
    Age)
from user.models   import User

class ProductView(View):
    @login_decorator
    def post(self, request):
        try:
            data              = json.loads(request.POST['body'])
            login_user        = request.user

            brand             = data['brand']
            category          = data['category']
            title             = data['title']
            price             = data['price']
            introduction      = data['detail_category']
            available_now     = data.get('now', False)
            thumbnail_url     = data['thumbnail']
            age               = data['age']
            class_level       = data['level']
            gender            = data['gender']
            product_image     = data['image']
            description       = data['description']
            gift              = data.get('gift', False)
            satisfaction      = data.get('satisfaction', 90)
#
            brand       =  Brand.objects.filter(id=brand)
            category    = Category.objects.filter(id=category)
            class_level = ClassLevel.objects.filter(name=class_level).first()
            login_user  = User.objects.get(id=login_user)

            product = Product.objects.create(
                    title             = title,
                    price             = price,
                    gift              = gift,
                    available_now     = available_now,
                    introduction      = introduction,
                    thumbnail_url     = thumbnail_url,
                    user              = login_user,
                    category          = category.first(),
                    satisfaction      = satisfaction,
                    class_level       = class_level
                    )
        
            if age:
                product.age.add(Age.objects.get(group=age))
        
            Gender.objects.create(
                    name = gender,
                    product= product
                    )
        
            ProductImage.objects.create(
                    name=product_image,
                    product = product
                    )
            return JsonResponse({"MESSAGE" : "SUCCESS"}, status=200)

        except KeyError:
           return JsonResponse({"MESSAGE" : "INVALID_KEY"}, status=400)


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
    @login_check
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

class LikeView(View):
    @login_decorator
    def post(self, request, product_id):
        user = request.user
        
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({"MESSAGE":"PRODUCT_DOES_NOT_EXISTS"}, status=200)
        
        if not ProductUserlike.objects.filter(Q(user_id=user.id)&Q(product_id=product_id)).exists():
            ProductUserlike.objects.create(user_id=user.id, product_id=product_id)
        else:
            product_user_like = ProductUserlike.objects.get(Q(user_id=user.id)&Q(product_id=product_id))
            product_user_like.is_liked = not product_user_like.is_liked
            product_user_like.save()

        return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)