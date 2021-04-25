

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="WorkArtDesignAPI",
      default_version='v1',
      description="Backend para workartdesign taller numero 2 para el ingeniero Juan Fajardo",
      contact=openapi.Contact(email="jorgecuenca.unity@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^typepainting/',include('typepainting.urls')),
    re_path(r'^leveldamage/',include('leveldamage.urls')),
    re_path(r'^categorydamage/',include('categorydamage.urls')),
    re_path(r'^costrestauration/',include('costrestauration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]