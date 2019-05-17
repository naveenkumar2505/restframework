from rest_framework import serializers
from productapp import models

class ProductInfoSeriliazer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'pno',
            'pname',
            'pcost',
            'pdesc'
        )
        model=models.ProductInfo