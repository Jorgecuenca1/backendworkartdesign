from django.urls import path, re_path

from . import views

urlpatterns =[
    re_path(r'^api/categorydamage$', views.categorydamage_list),
    re_path(r'^api/categorydamage/(?P<pk>[0-9]+)$', views.categorydamage_detail),
]