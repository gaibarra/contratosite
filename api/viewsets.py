from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from cto.models import Contratos
from api.serializer import ContratosSerializer, TipocontratoSerializer

class ContratosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer

    def perform_update(self, serializer):
        tipo = serializer.validated_data.get("tipocontrato")
        if tipo is not None and tipo.pk != serializer.instance.tipocontrato_id:
            raise ValidationError({"tipocontrato": "El tipo de contrato no puede modificarse desde la aplicación."})
        serializer.save()

class TipocontratoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Contratos.objects.all()
    serializer_class = TipocontratoSerializer
