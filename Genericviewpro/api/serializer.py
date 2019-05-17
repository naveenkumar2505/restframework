from rest_framework import serializers
from productapp import models

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model=models.Product

        fields=(
            'product_id',
            'product_name',
            'product_cost',
            'product_desc',
        )