from django.db import models
from gestion.models import Plan

# Create your models here.
class Modulo(models.Model):

    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.numero}"

class TipoUnidad(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class UnidadDidactica(models.Model):

    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoUnidad, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    ciclo = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class TipoCompetencia(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Competencia(models.Model):

    tipo = models.ForeignKey(TipoCompetencia, on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadDidactica, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Capacidad(models.Model):

    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Indicador(models.Model):

    capacidad = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Contenido(models.Model):

    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
