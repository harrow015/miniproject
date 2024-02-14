from django.db import models

# Create your models here.
class seller_table(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default='null')
    image = models.FileField(max_length=20)
    status = models.CharField(max_length=20, default='pending')


class product_table(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(max_length=20)
    price = models.CharField(max_length=20)
    details = models.CharField(max_length=20)
    stock = models.IntegerField()
    seller_id = models.ForeignKey(seller_table,on_delete=models.CASCADE)
    category_id = models.ForeignKey('site_admin.category_tb',on_delete=models.CASCADE)


class tracking_table(models.Model):
    orderid=models.ForeignKey('buyer.order_table',on_delete=models.CASCADE)
    date= models.CharField(max_length=20) 
    time=models.CharField(max_length=20)
    details=models.CharField(max_length=20)



