from rest_framework import status
from rest_framework.response import Response
from .models import Emp
from .serializers import EmpSerializer
from rest_framework.views import APIView
class EmpView(APIView):
    def get(self,request):
        emp=Emp.objects.all()
        serializer=EmpSerializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            employee_name=serializer.data.get('employee_name')
            employee_salary=serializer.data.get('salary_name')
            msg='Hello {},your salary is {}'.format(employee_name,employee_salary)
            emp=Emp.objects.create(employee_name=employee_name,employee_salary=employee_salary)
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)