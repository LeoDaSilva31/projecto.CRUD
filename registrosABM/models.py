from django.db import models

# Create your models here.
class Persona(models.Model):
    dni=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=8)
    edad=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} {1} {2} (edad: {3})"
        return texto.format(self.dni, self.nombre, self.apellido, self.edad)