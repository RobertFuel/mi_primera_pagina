from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "producto"

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_form"),
]
