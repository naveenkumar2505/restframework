from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import ViewsetsStudent

router=DefaultRouter()

router.register('student_view',ViewsetsStudent,base_name='viewsets')

urlpatterns=[
    url(r'',include(router.urls))
]