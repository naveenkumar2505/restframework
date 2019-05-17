#username=tokenbased password=qwerty1234

from django.contrib import admin
from .models import Emp
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['emid','empname','empsal','created','modified']

admin.site.register(Emp,EmpAdmin)