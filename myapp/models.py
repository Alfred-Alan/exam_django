from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200,verbose_name="用户名")
    password=models.CharField(max_length=200,verbose_name="密码")
    class Meta:
        db_table="User"

class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    des = models.CharField(max_length=200)
    class Meta:
        db_table="goods"