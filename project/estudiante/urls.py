from django.urls import path

from . import views

app_name = "estudiante"

urlpatterns = [
    path("", views.index, name="index"),
    path("crearen/", views.crearen, name="crearen"),
    path("crearfr/", views.crearfr, name="crearfr"),
    path("creares/", views.creares, name="creares"),
    path("crearpais/", views.crearpais, name="crearpais"),
]
