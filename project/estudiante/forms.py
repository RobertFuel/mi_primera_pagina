from django import forms

from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.EstudianteEN
        fields = ["nombre", "apellido", "nacimiento", "nacionalidad"]
        
class Estudiante2Form(forms.ModelForm):
    class Meta:
        model = models.EstudianteES
        fields = ["nombre", "apellido", "nacimiento", "nacionalidad"]
        
class Estudiante3Form(forms.ModelForm):
    class Meta:
        model = models.EstudianteFR
        fields = ["nombre", "apellido", "nacimiento", "nacionalidad"]