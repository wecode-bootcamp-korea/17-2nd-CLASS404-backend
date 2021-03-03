from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'brands'

class Category(models.Model):
    name = models.CharField(max_length=45)
    brand = models.ForeignKey('brand', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class PreperationKit(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table= 'preperation_kits'

class Gender(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table= 'genders'

class UserLevel(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'user_levels'

class ProductImage(models.Model):
    name = models.URLField(max_length=2000)

    class Meta:
        db_table = 'product_images'

class PromotionCoupon(models.Model):
    code           = models.IntegerField()
    discount_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'promotion_coupons'

class ClassSatisfaction(models.Model):
    name = models.IntegerField()

    class Meta:
        db_table = 'class_satisfactions'

class Age(models.Model):
    group = models.CharField(max_length=45)

    class Meta:
        db_table = 'ages'

class Product(models.Model):
    title              = models.CharField(max_length=200)
    price              = models.DecimalField(max_digits=12, decimal_places=2)
    gift               = models.BooleanField(default=True)
    available_now      = models.BooleanField(default=True)
    introduction       = models.TextField()
    user_contents      = models.BooleanField(default=True)
    thumbnail_url      = models.URLField(max_length=2000)
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    closing_date       = models.DateTimeField()
    category           = models.ForeignKey('category', on_delete=models.CASCADE)
    user               = models.ForeignKey('user.User', on_delete=models.CASCADE)
    preperation_kit    = models.ForeignKey('PreperationKit', on_delete=models.SET_NULL,null=True)
    user_level         = models.ForeignKey('UserLevel', on_delete=models.SET_NULL, null=True)
    class_satisfaction = models.ForeignKey('ClassSatisfaction', on_delete=models.SET_NULL,null=True)
    product_images     = models.ForeignKey('ProductImage',on_delete=models.SET_NULL, null=True)
    promotion_coupon  = models.ForeignKey('PromotionCoupon', on_delete=models.SET_NULL,null=True)
    gender             = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    age                = models.ManyToManyField('Age', through='ProductAge', related_name='age')
    description        = models.TextField()


    class Meta:
        db_table = 'products'

class ProductAge(models.Model):
    product = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True)
    age     = models.ForeignKey('Age', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_ages'
            

class ProductUserlike(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user    = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Mata:
        db_table = 'product_user_likes'


class Review(models.Model):
    image_url   = models.URLField(max_length=2000)
    description = models.TextField()
    user        = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'
