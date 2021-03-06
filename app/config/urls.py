"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
        contact=openapi.Contact(email='qjaduddl942@gmail.com')
    )
)

urlpatterns = [
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('users/', include('members.urls')),
    path('api_fbv_v1/', include('snippets.urls.fbv_urls_v1')),
    path('api_fbv_v2/', include('snippets.urls.fbv_urls_v2')),
    path('api_cbv_apiview/', include('snippets.urls.cbv_urls_apiview')),
    path('api_cbv_mixins/', include('snippets.urls.cbv_urls_mixins')),
    path('api_cbv_generic/', include('snippets.urls.cbv_urls_generic')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
