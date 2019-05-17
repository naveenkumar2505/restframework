from django.db import models
class Product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    pcost=models.FloatField()
    pdesc=models.CharField(max_length=100)


