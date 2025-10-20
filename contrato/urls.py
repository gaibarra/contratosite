"""formatmodelo URL Configuration

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
import debug_toolbar
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.templatetags.static import static as static_url
#from cto import views





urlpatterns = [

    path('', include(('bases.urls', 'bases'), namespace='bases')),
    path('cto/', include(('cto.urls', 'cto'), namespace='cto')),
    path('ley/', include(('ley.urls', 'ley'), namespace='ley')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    # Favicon for browsers that request /favicon.ico
    path('favicon.ico', RedirectView.as_view(url=static_url('favicon.ico'), permanent=True)),
    
  
    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

if settings.DEBUG:
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns