from django.db import models

class Admin_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class Category_tb(models.Model):
    categoryname=models.CharField(max_length=20)
# Create your models here.
