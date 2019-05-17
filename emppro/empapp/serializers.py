from rest_framework import serializers
class EmpSerializers(serializers.Serializer):
    ename=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=50)