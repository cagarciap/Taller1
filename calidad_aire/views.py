from django.shortcuts import render
from rest_framework import viewsets
from .models import calidad_aire
from .serializers import Calidad_aireSerializer

class calidad_aireViewSet(viewsets.ModelViewSet):
    queryset = calidad_aire.objects.all().order_by('-created')
    serializer_class = Calidad_aireSerializer
# Create your views here.
