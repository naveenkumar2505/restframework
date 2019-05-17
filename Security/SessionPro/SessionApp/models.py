from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=100)
    scourse=models.CharField(max_length=100)
    cfee=models.IntegerField()

    def __str__(self):
        return self.sname
