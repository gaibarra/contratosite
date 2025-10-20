from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
#from .reportes import imprimir_solicitud, imprimir_archivos

urlpatterns = [
    
    #path('upload/',upload, name="upload"),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns