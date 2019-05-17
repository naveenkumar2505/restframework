from django.conf.urls import url
from django.contrib import admin
from empapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emp/',views.EmpView.as_view())
]
