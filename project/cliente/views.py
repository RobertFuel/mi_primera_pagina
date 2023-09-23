from django.shortcuts import render


def index(request):
    contexto = {"nombre": "Cliente"}
    return render(request, "cliente/index.html", contexto)