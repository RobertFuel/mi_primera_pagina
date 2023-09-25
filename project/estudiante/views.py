from django.shortcuts import redirect, render

from . import models, forms

def index(request):
    estudiantesEN = models.EstudianteEN.objects.all()
    estudiantesES = models.EstudianteES.objects.all()
    estudiantesFR = models.EstudianteFR.objects.all()
    return render(request, "estudiante/index.html", {"estudiantesEN":estudiantesEN, "estudiantesES":estudiantesES, "estudiantesFR":estudiantesFR})

def crearen(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.EstudianteForm()
    return render(request, "estudiante/crearen.html", {"form": form})

def creares(request):
    if request.method == "POST":
        form = forms.Estudiante2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.Estudiante2Form()
    return render(request, "estudiante/creares.html", {"form": form})

def crearfr(request):
    if request.method == "POST":
        form = forms.Estudiante3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.Estudiante3Form()
    return render(request, "estudiante/crearfr.html", {"form": form})
    