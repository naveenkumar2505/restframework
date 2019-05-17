from django.contrib import admin
from .models import Emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ['emp_id',
                    'ename',
                    'salary',
                    'email']
admin.site.register(Emp,EmpAdmin)