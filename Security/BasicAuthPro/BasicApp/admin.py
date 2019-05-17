#uname=basic pwd=qwerty1234

from django.contrib import admin

from BasicApp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','course','fee']

admin.site.register(Student,StudentAdmin)
