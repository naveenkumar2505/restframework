from rest_framework import serializers
from .models import Emp

class Serializer_Emp(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields= ('emp_id',
                 'ename',
                 'salary',
                 'email')
