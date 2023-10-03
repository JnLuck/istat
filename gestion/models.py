from django.db import models

# Create your models here.

class Institucion(models.Model):

    nombre = models.CharField(max_length=50)
    logo = models.ImageField(blank=True)
    lugar = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Carrera(models.Model):

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plan(models.Model):

    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
