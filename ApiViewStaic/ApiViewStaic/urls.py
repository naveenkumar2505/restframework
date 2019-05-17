from django.conf.urls import url
from django.contrib import admin
from ApiViewStaicapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ins/',views.Institute.as_view())
]
