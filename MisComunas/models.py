from django.db import models

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    poblacion = models.IntegerField()
    tasa_vulnerabilidad = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_fundacion = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    

