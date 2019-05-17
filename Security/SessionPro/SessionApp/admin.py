#username===session password===qwerty1234

from django.contrib import admin

# Register your models here.
from SessionApp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','scourse','cfee']

admin.site.register(Student,StudentAdmin)
