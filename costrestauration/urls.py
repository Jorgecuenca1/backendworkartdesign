from django.urls import path, re_path

from . import views

urlpatterns =[
    re_path(r'^api/costrestauration$', views.costrestauration_list),
    re_path(r'^api/costrestauration/(?P<pk>[0-9]+)$', views.costrestauration_detail),
]