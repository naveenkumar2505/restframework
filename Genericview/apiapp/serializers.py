from rest_framework import serializers
from productapp import models
class PS(serializers.ModelSerializer):
    class Meta:
        fields=(
            'pno',
            'pname',
            'pcost',
            'pdesc'
        )
        model=models.Product