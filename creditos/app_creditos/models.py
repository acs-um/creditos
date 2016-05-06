from django.db import models

# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField("nombre", max_length=255)
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

    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    codigo = models.IntegerField("codigo", primary_key=True)
    nombre = models.CharField("nombre", max_length=255)
    creditos = models.PositiveSmallIntegerField("creditos")
    año = models.PositiveSmallIntegerField("año")
#    correlativas = models.ForeignKey("Materia", )

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre
