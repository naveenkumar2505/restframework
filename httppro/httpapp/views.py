from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
#Way1 to convert static data into Json
# def httpview(request):
#     emp_data={
#         'eno':100,
#         'ename':'Naveen',
#         'esal':10000,
#         'com':'tcs'
#     }
#     resp='<h1>Employee number:{}<br>' \
#          'Employee Name is:{}<br>' \
#          'Employee salary is:{}<br>' \
#          'Employee company is:{}<br></h1>'.format(emp_data['eno'],
#                                                   emp_data['ename'],
#                                                   emp_data['esal'],
#                                                   emp_data['com'])
#     return HttpResponse(resp)
def emp_data_view(request):
    emp_data={
        'eno':100,
        'ename':'Naveen',
        'email':'naveen@gmail.com',
        'salary':10000
    }
    return JsonResponse(emp_data)