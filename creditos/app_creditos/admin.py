from django.contrib import admin
from .models import Carrera, Secretario, Alumno


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass


@admin.register(Secretario)
class SecretarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass

