from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from . import models, forms

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    
class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    
class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
