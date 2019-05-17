from django.db import models
class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=20)
    product_cost=models.FloatField()
    product_desc=models.CharField(max_length=50)


