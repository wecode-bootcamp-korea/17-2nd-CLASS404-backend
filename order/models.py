from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_statuses'

class Address(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'addresses'

class Order(models.Model):
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    status     = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    user       = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    address    = models.ForeignKey('Address', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders'

