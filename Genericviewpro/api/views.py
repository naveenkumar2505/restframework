from django.shortcuts import render
from rest_framework import generics
from productapp import models
from . import serializer
class ListProduct(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
class ListDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer