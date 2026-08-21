from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import CambioContrasenaView, Home, HomeSinPrivilegios, healthz


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('healthz', healthz, name='healthz'),
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),
        name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='bases/login.html'),
        name='logout'),
    path('cambiar-contrasena/', CambioContrasenaView.as_view(), name='cambiar_contrasena'),

    path('sin_privilegios/',
         HomeSinPrivilegios.as_view(),
         name='sin_privilegios')
]
