from django.shortcuts import render
from .models import Emp
from .serializers import Serializer_Emp
from rest_framework import viewsets

class Modelviews_Emp(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class = Serializer_Emp

