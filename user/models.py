from django.db      import models

class UserTier(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'user_tiers'

class UserType(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'user_types'
        
class CreatorInfo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'creator_info'        

class User(models.Model):
    name         = models.CharField(max_length=45)
    email        = models.EmailField(max_length=500, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    image_url    = models.URLField(max_length=2000, default="https://media.vlpt.us/images/c_hyun403/post/7b35d3bb-44be-41bf-8192-0ccc426b465c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-02-26%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.53.02.png")
    nickname     = models.CharField(max_length=45, null=True)
    social_login = models.CharField(max_length=50, null=True)
    tier         = models.ForeignKey('UserTier', on_delete=models.CASCADE)
    user_type    = models.ForeignKey('UserType', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'users'

