from django.db import models

from estudiantes.models import Estudiante

# Create your models here.
class CertificadoModular(models.Model):

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.estudiante.persona.nombre}"

class TipoEducacion(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CertificadoEducacion(models.Model):

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoEducacion, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    registro_minedu = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.estudiante.persona.nombre}"
    
class TipoAuxiliar(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CertificadoAuxiliar(models.Model):

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoAuxiliar, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.estudiante.persona.nombre}"
