from django.db import models
class Emp(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_salary=models.BigIntegerField()
