from django.db import models

class Student(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    sname=models.CharField(max_length=250)
    course=models.CharField(max_length=50)
    fee=models.IntegerField()

    def __str__(self):
        return self.sname