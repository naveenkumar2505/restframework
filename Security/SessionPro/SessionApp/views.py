# from django.contrib.auth import login,authenticate
# from django.shortcuts import render, redirect
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ModelViewSet
# from .models import Student
# from .serializers import StudenSerializer
# # Create your views here.
#
# def login_form(request):
#     return render(request,'login.html')
#
# def login_user(request):
#     usern=request.POST['uname']
#     pasw=request.POST['pwd']
#
#     user=authenticate(username=usern,password=pasw)
#     if user is not None:
#         login(request,user)
#         #return redirect('/auth')
#         return redirect('/api')
#     else:
#         #return redirect('/api')
#         return redirect('/auth')
#
# class StudentView(ModelViewSet):
#     authentication_class=(SessionAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Student.objects.all()
#     serializer_class = StudenSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .serializers import StudenSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

def login_form(request):
    return render(request, 'login.html')

def login_user(request):
    username = request.POST['uname']
    password = request.POST['pwd']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/api')
    else:
        return redirect('/auth')

class StudentView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Student.objects.all()
    serializer_class = StudenSerializer
