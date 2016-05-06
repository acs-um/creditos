from django import forms
from .models import Carrera, Alumno, Secretario


class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ('nombre', 'años_de_duracion', 'secretario')


class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('legajo', 'nombre', 'apellido', 'dni', 'mail', 'carrera')


class SecretarioForm(forms.ModelForm):

    class Meta:
        model = Secretario
        fields = ('nombre',)
