from .models import Emp
from .serializers import EmpSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
class EmpView(APIView):
    def get(self,request):
        employee_details=Emp.objects.all()
        serializer=EmpSerializers(employee_details,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmpSerializers(data=request.data)
        if serializer.is_valid():
            ename=serializer.data.get('ename')
            email=serializer.data.get('email')
            msg="Hello {}, your mail id is {}".format(ename,email)
            Emp.objects.create(ename=ename,email=email)
            return Response({'message':msg})
        else:
            return Response(serializer.error)