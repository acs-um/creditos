from django.db import models

# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField("nombre", max_length=255)
    años_de_duracion = models.PositiveSmallIntegerField("años de duracion")
    secretario = models.ForeignKey("Secretario", verbose_name="Secretario", related_name="Carreras")

    class Meta:  # define los metadatos del modelo. como se va a mostrar, como se ordena, etc
        verbose_name = "carrera"
        verbose_name_plural = "carreras"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Secretario(models.Model):
    nombre = models.CharField("apellido", max_length=255)

    class Meta:
        verbose_name = "secretario"
        verbose_name_plural = "secretarios"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre
