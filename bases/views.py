from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.views import generic


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"


class CambioContrasenaView(PasswordChangeView):
    """Permite a cualquier usuario autenticado cambiar únicamente su contraseña."""

    template_name = "bases/change_password.html"
    success_url = reverse_lazy("bases:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tu contraseña se actualizó correctamente.")
        return response


def healthz(request):
    return HttpResponse("ok-contratos", content_type="text/plain")
