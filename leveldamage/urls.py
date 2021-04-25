from django.urls import path, re_path

from . import views

urlpatterns =[
    re_path(r'^api/leveldamage$', views.leveldamage_list),
    re_path(r'^api/leveldamage/(?P<pk>[0-9]+)$', views.leveldamage_detail),
]