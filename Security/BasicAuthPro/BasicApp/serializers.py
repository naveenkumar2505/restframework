from rest_framework import serializers

from BasicApp import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=('id','sname','course','fee')
