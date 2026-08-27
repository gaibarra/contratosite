from django.shortcuts import render
from requests.api import put

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.serializer import ContratosSerializer, TipocontratoSerializer
from cto.models import Contratos, Tipocontrato

from django.db.models import Q

class ContratosList(APIView):
    def get(self,request):
        cont = Contratos.objects.all()
        data =ContratosSerializer(cont,many=True).data
        return Response(data)


class ContratosDetalle(APIView):
    def get(self,request, id):
        cont = get_object_or_404(Contratos,Q(id=id))
        data = ContratosSerializer(cont).data
        return Response(data)

class TipocontratoDetalle(APIView):
    def get(self,request, id):
        cont = get_object_or_404(Tipocontrato,Q(id=id))
        data = TipocontratoSerializer(cont).data
        xdata = data
        return Response(data)
    
    def post(self,request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self,request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
