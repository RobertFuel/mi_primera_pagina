from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "Productos"
admin.site.site_header = "Multilingo"

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    
@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre", 
        "unidad_de_medida", 
        "cantidad", 
        "precio", 
        "descripcion", 
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre",
    )
    list_filter = (
        "categoria",
    )
    date_hierarchy = "fecha_actualizacion"
    