from django.shortcuts import render
from rest_framework import mixins,generics
from .serializers import ProductSerializer
from .models import Product

class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ProductDetails(mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(self,request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(self,request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(self,request,*args,**kwargs)



