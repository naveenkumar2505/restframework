from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^application/',include('apiapp.urls')),
    #url(r'api-auth/',include('rest_framework.urls'))
]
