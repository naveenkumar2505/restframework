from django.contrib import admin
from .models import Emp
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','employee_salary']
admin.site.register(Emp,EmployeeAdmin)
