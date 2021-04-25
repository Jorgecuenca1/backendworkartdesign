from django.urls import path, re_path

from . import views

urlpatterns =[
    re_path(r'^api/typepainting$', views.typepainting_list),
    re_path(r'^api/typepainting/(?P<pk>[0-9]+)$', views.typepainting_detail),
]