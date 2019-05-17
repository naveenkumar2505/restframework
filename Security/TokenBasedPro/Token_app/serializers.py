from rest_framework import serializers
from .models import Emp

class Emp_Serializers(serializers.ModelSerializer):
    class Meta:
        models=Emp
        fields='__all__'
