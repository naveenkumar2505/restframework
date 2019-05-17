from django.shortcuts import render
from rest_framework import generics
from productapp import models
from . import serializers
class ListProduct(generics.ListCreateAPIView):
    queryset=models.ProductInfo.objects.all()
    serializer_class=serializers.ProductInfoSeriliazer
