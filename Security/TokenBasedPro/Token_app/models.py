from django.db import models

# Create your models here.
class Emp(models.Model):
    emid=models.AutoField(primary_key=True)
    empname=models.CharField(max_length=100)
    empsal=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.empname