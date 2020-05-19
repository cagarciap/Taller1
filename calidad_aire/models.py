from django.db import models
import uuid

class calidad_aire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, verbose_name='Codigo', default="x")
    latitud = models.FloatField(verbose_name='Latitud', default=0)
    longitud = models.FloatField(verbose_name='Longitud', default=0)
    producto = models.CharField(verbose_name='Producto', max_length=20, default="x")
    area = models.FloatField(verbose_name='Area', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# Create your models here.
