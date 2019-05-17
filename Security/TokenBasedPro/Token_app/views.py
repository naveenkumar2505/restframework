from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .models import Emp
from .serializers import Emp_Serializers

# Create your views here.
def login_form(request):
    return render(request,'login.html')

def login_user(request):
    uname=request.POST['uname']
    pwd=request.POST['pwd']

    user=authenticate(username=uname,password=pwd)

    if user is not None:
        login(request,user)
        return redirect('/api')
    else:
        return redirect('/auth')

class Emp_views(ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class = Emp_Serializers
