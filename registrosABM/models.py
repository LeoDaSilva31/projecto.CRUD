from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=8)
    dni_pasaporte = models.CharField(max_length=20)
    fecha_entrada = models.DateField(null=True, blank=True)
    fecha_salida = models.DateField(null=True, blank=True)
    numero_habitacion = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5}"
        return texto.format(self.nombre, self.apellido, self.dni_pasaporte, self.numero_habitacion, self.fecha_entrada, self.fecha_salida)