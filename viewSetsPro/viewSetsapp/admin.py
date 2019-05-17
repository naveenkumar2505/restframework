from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['user_id','name',
                    'email','subject',
                    'message','created',
                    'modified']

admin.site.register(Feedback,FeedbackAdmin)


