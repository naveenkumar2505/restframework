from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from SessionApp.views import StudentView
router=DefaultRouter()
router.register('students',StudentView,base_name='students')

urlpatterns=[
    url(r'',include(router.urls))
]