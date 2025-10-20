from .models import Tipocontrato
from django.db import transaction, IntegrityError
from django.http import HttpRequest
import json


class CtoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(request.META)
        self.process_request(request)
        response = self.get_response(request)
        return response

    # def process_view(self,request, view_func, view_args, view_kwargs):
    #     url = request.META.get('PATH_INFO')
    #     #print(url)
    #     if request.user.is_authenticated:
    #         if 'api' in url:
    #              xid = (view_kwargs['id'])
    #              #print (xid)
    #              #print('esta es', request, view_func, view_args, view_kwars)
    #              tipocontrato = Tipocontrato.objects.filter(estado=True)
    #              for tipo in tipocontrato:
    #                  #print(type(tipo.id))
    #                  #print(type(xid))
    #                  if str(tipo.id) == xid:
    #                     tipo.marcatipoContrato = True
    #                     tipo.save()
    #                  else:
    #                     tipo.marcatipoContrato = False
    #                     tipo.save()

    def process_request(self, request: HttpRequest):
        url = request.META.get("PATH_INFO", "")
        # Solo actuar en rutas de API POST/PUT/PATCH donde esperamos un id en el body
        if not url or "api" not in url or request.method not in {"POST", "PUT", "PATCH"}:
            return None

        # Intentar extraer "id" del body (JSON o texto simple) o de la URL /.../<id>
        xid = None
        try:
            if request.body:
                # Primero intenta JSON {"id": 123}
                data = json.loads(request.body.decode("utf-8"))
                if isinstance(data, dict) and "id" in data:
                    xid = data["id"]
                elif isinstance(data, (str, int)):
                    xid = data
        except Exception:
            # Si no es JSON válido, considerar todo el body como el id en texto
            try:
                xid = request.body.decode("utf-8").strip()
            except Exception:
                xid = None

        if not xid:
            # Fallback: intentar extraer el último segmento numérico de la URL
            try:
                parts = [p for p in url.split('/') if p]
                if parts:
                    candidate = parts[-1]
                    if candidate.isdigit():
                        xid = int(candidate)
            except Exception:
                pass
        if not xid:
            return None

        # Operación atómica y con protección ante condición de carrera
        try:
            with transaction.atomic():
                # Bloquear los actualmente activos para evitar carreras
                list(
                    Tipocontrato.objects.select_for_update()
                    .filter(estado=True, marcatipoContrato=True)
                )
                # Apagar los activos actuales
                Tipocontrato.objects.filter(estado=True, marcatipoContrato=True).update(
                    marcatipoContrato=False
                )
                # Bloquear y encender el solicitado
                list(
                    Tipocontrato.objects.select_for_update().filter(estado=True, id=xid)
                )
                Tipocontrato.objects.filter(estado=True, id=xid).update(marcatipoContrato=True)
        except IntegrityError:
            # Si la constraint de unicidad se dispara por carrera, reintentar una vez limpiando y marcando
            with transaction.atomic():
                Tipocontrato.objects.filter(estado=True).update(marcatipoContrato=False)
                Tipocontrato.objects.filter(estado=True, id=xid).update(marcatipoContrato=True)
        return None
