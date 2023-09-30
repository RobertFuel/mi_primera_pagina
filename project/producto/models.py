from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripcion")
    
    class Meta:
        verbose_name = "categoria de productos"
        verbose_name_plural = "categorias de productos"
        
    def __str__(self) -> str:
        return self.nombre
    
class Producto(models.Model):
    """Productos que corresponde a una categoria"""
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoria")
    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        
    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio}"