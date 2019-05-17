from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import Modelviews_Emp

router=DefaultRouter()
router.register('',Modelviews_Emp,base_name='modelviews')

urlpatterns=router.urls

urlpatterns=[
    url(r'',include(router.urls))
]


#  api/urls.py
# from django.urls import path
#
# from . import TodoViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('', TodoViewSet, base_name='todos')
# urlpatterns = router.urls