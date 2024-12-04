from rest_framework import serializers
from .models import SolicitudAyuda

class SolicitudAyudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAyuda
        fields = ['correo', 'texto']  # Usuario se deriva del token
