from django.db import models
from django.contrib.auth.models import User


class Carrera(models.Model):
    nombre = models.CharField("nombre", max_length=255, unique=True)
    años_de_duracion = models.PositiveSmallIntegerField("años de duracion")
    secretario = models.ForeignKey("Secretario", verbose_name="Secretario", related_name="Carreras")
    estado = models.BooleanField(default=True)
    cantidad_alumnos = models.IntegerField(null=True)

    class Meta:  # define los metadatos del modelo. como se va a mostrar, como se ordena, etc
        verbose_name = "carrera"
        verbose_name_plural = "carreras"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Secretario(models.Model):
    nombre = models.CharField("apellido", max_length=255)
    estado = models.BooleanField(default=True)
    usuario = models.OneToOneField(User)

    class Meta:
        verbose_name = "secretario"
        verbose_name_plural = "secretarios"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    legajo = models.IntegerField("legajo", primary_key=True)
    nombre = models.CharField("nombre", max_length=255)
    apellido = models.CharField("apellido", max_length=255)
    dni = models.BigIntegerField("dni")
    mail = models.EmailField(max_length=255, null=True)
    estado = models.BooleanField(default=True)
    carrera = models.ForeignKey("Carrera", verbose_name="Carrera", related_name="Alumnos")
    usuario = models.OneToOneField(User)

    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ['nombre', ]

    def __str__(self):
        return '%s %s' %(self.nombre, self.apellido)


class Materia(models.Model):
    codigo = models.IntegerField("codigo", primary_key=True)
    nombre = models.CharField("nombre", max_length=255, unique=True)
    creditos = models.PositiveSmallIntegerField("creditos")
    año = models.PositiveSmallIntegerField("año")
    correlativas = models.ManyToManyField("Materia", verbose_name="correlativas", related_name="correlacion", blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre

