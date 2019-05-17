from django.conf.urls import url
from . import views

urlptterns=[
    url(r'',views.ListProduct.as_view())
]