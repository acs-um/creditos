from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Secretario, Carrera, Alumno


# deben poder guardarse los secretarios correctamente
class SecretarioTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_crear_secretario(self):
        Secretario.objects.create(nombre="lucas_test")
        Secretario.objects.create(nombre="gaston_test")
        resp = self.client.get(reverse('app_creditos:secretario_list'))
        self.assertEqual(len(resp.context["object_list"]), 2)

        secretario = Secretario.objects.get(nombre="lucas_test")
        secretario.estado = False
        secretario.save()
        resp = self.client.get(reverse('app_creditos:secretario_list'))
        self.assertEqual(len(resp.context["object_list"]), 1)

    def test_edit_secretario(self):
        secre = Secretario.objects.create(nombre="joel_test")

        resp = self.client.post(reverse('app_creditos:secretario_edit', kwargs={'pk': secre.pk}), {
            'nombre': "Joel",
            'estado': True
        })
        self.assertRedirects(resp, reverse('app_creditos:secretario_list'), status_code=302)

        secre2 = Secretario.objects.get(pk=secre.pk)
        self.assertEqual(secre2.nombre, "Joel")


class CarreraTestCase(TestCase):
    def setUp(self):
        self.carrera = Carrera.objects.create(nombre="ing quimica_test", años_de_duracion=5, secretario=Secretario.objects.create(
            nombre="claudio_test"))
        self.client = Client()

        self.alumno = Alumno.objects.create(legajo=1234, nombre="Alvaro", apellido="Gonzalez", dni=12345678,
                              carrera=Carrera.objects.get(nombre="ing quimica_test"))

    def test_crear_carrera(self):
        # carrera = Carrera.objects.get(nombre="ing quimica_test")
        self.assertEqual(self.carrera.nombre, "ing quimica_test")
        self.assertEqual(self.carrera.secretario.nombre, "claudio_test")
        self.assertEqual(self.carrera.años_de_duracion, 5)

    def test_cantidad_alumnos(self):
        resp = self.client.get(reverse('app_creditos:index'))
        self.assertEqual(resp.context["carreras"].count(), 1)
        self.assertEqual(resp.context['carreras'].get().contidad_alumnos, 1)


class AlumnoTestCase(TestCase):
    def setUp(self):
    # crear carrera

    def crear_alumno(self):
        carrera = Carrera.objects.get(nombre="ing quimica_test")
        # hacer un get del la vista client.get
        # que status_code es 200
        # use tal template self.assertTemplateUsed()
        # haya un form self.assertTrue()
        resp = self.client.post(reverse('app_creditos:alumno_new', {
            'legajo': 5967,
            'nombre': "Alverto",
            'apellido': "Gonzalez",
            'dni': 35623147,
            'carrera': carrera
        }))
        # despues de guardar hace un response 302
        # comprobar contra la db si se guardo el alumno
        # hacer otro post con errores de validacion
        resp = self.client.post(reverse('app_creditos:alumno_new', {
            'nombre': "Alverto1",
            'apellido': "Gonzalez1",
            'dni': 35623146,
            'carrera': carrera
        }))
        self.assertTrue("legajo" in resp.context["form"].errors)