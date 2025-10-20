from rest_framework import serializers
from cto.models import Contratos, Tipocontrato


class ContratosSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contratos
        fields='__all__'

class TipocontratoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Tipocontrato
        fields='__all__'