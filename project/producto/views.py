from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    
    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.ProductoCategoria.objects.filter(
                nombre__icontains=consulta
            )
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list
    
class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    
class ProductoCategoriaCreate(CreateView, LoginRequiredMixin):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
class ProductoCategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
class ProductoCategoriaDelete(DeleteView, LoginRequiredMixin):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    
