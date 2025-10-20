from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *
from .viewsets import ContratosViewSet, TipocontratoViewSet

router = routers.SimpleRouter()
router.register(r'contratos', ContratosViewSet, TipocontratoViewSet)


urlpatterns = [
    path('v1/contratos/',ContratosList.as_view(),name='contratos_list'),
    path('v1/contratos/<str:id>',ContratosDetalle.as_view(),name='contratos_detalle'),
    path('v1/tipocontrato/<str:id>',TipocontratoDetalle.as_view(),name='tipocontrato_detalle'),
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]