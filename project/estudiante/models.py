from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nombre
    
class EstudianteEN(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class EstudianteES(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class EstudianteFR(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
