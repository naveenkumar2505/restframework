from django.conf.urls import url
from django.conf.urls import include
from .views import Viewset_Feedback
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'user',Viewset_Feedback,base_name='viewset')

urlpatterns=router.urls


urlpatterns = [
    url(r'',include(router.urls))
     ]

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# urlpatterns = router.urls