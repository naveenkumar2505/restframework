from rest_framework import serializers
class EmpSerializer(serializers.Serializer):
    employee_name=serializers.CharField(max_length=50)
    employee_salary=serializers.IntegerField()