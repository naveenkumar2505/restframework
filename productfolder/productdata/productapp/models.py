from django.db import models

class ProductInfo(models.Model):
    pno=models.IntegerField()
    pname=models.CharField(max_length=20)
    pcost=models.IntegerField()
    pdesc=models.CharField(max_length=20)
    def __str__(self):
        return self.pname