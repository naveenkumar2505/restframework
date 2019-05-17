from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    salary=models.BigIntegerField()
    company=models.CharField(max_length=30)
