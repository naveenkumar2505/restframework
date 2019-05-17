from django.db import models

class Feedback(models.Model):

    user_id=models.IntegerField()
    name=models.CharField(max_length=50,help_text='Name of the sender')
    email=models.EmailField(max_length=100,unique=True)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name +'__'+self.email
