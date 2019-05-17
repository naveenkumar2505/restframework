from django.conf.urls import url
from api import views
urlpatterns=[
    url(r'^product/$',views.ListProduct.as_view()),
    url(r'^product/(?P<pk>[0-9]+)',views.ListDetails.as_view())
]

#another way to Urls
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.ListProduct.as_view()),
#     path('<int:pk>/', views.ListDetail.as_view()),
# ]