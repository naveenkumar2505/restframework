from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from Token_app.views import Emp_views

router=DefaultRouter()
router.register('emp-view',Emp_views)

urlpatterns=[
    url(r'',include(router.urls))
]