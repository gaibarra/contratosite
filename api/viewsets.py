from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from cto.models import Contratos
from api.serializer import ContratosSerializer, TipocontratoSerializer

class ContratosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer

class TipocontratoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Contratos.objects.all()
    serializer_class = TipocontratoSerializer  
    