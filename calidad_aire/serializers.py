from rest_framework import serializers
from .models import calidad_aire

class Calidad_aireSerializer(serializers.ModelSerializer):
    class Meta:
        model = calidad_aire
        fields = ('id', 'type', 'value')