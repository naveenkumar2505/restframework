from django.contrib import admin
from .models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','email','salary','company']
admin.site.register(Employee,EmployeeAdmin)
