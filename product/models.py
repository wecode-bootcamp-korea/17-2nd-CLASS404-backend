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


class Gender(models.Model):
    name = models.CharField(max_length=45)
    product =models.ForeignKey('product', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table= 'genders'

class ClassLevel(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'class_levels'

class ProductImage(models.Model):
    name = models.URLField(max_length=2000)
    product = models.ForeignKey('product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_images'

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
    thumbnail_url      = models.URLField(max_length=2000)
    description        = models.TextField()
    satisfaction       = models.IntegerField()
    description        = models.TextField()
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    category           = models.ForeignKey('category', on_delete=models.CASCADE)
    user               = models.ForeignKey('user.User', on_delete=models.CASCADE)
    class_level        = models.ForeignKey('ClassLevel', on_delete=models.SET_NULL, null=True)
    age                = models.ManyToManyField('Age', through='ProductAge', related_name='age')


    class Meta:
        db_table = 'products'

class ProductAge(models.Model):
    product = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True)
    age     = models.ForeignKey('Age', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_ages'
            

class ProductUserlike(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    user     = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_user_likes'


class Review(models.Model):
    image_url   = models.URLField(max_length=2000)
    description = models.TextField()
    user        = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'
