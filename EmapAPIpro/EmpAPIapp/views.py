from .models import Employee
from django.http import JsonResponse
def adminview(request):
    emp_data=Employee.objects.all()
    data={'result':list(emp_data.values('eno','ename','email','salary','company'))}
    return JsonResponse(data)

