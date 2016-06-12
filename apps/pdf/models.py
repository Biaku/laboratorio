from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PDF_File(models.Model):
    archivo = models.FileField(upload_to='pdf')
    fecha_carga = models.DateTimeField(auto_now_add=True)


class CSV_File(models.Model):
    archivo = models.FileField(upload_to='csv')
    fecha_carga = models.DateTimeField(auto_now_add=True)


# este modelo es el que asociara los pdf al paciente
class Visualizar(models.Model):
    usuario = models.ForeignKey(User)
    ruta_pdf = models.CharField(max_length=50)
