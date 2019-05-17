from django.db import models

class Emp(models.Model):

    emp_id=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    salary=models.BigIntegerField()

