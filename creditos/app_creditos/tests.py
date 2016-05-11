from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Secretario, Carrera


# deben poder guardarse los secretarios correctamente
class SecretarioTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_crear_secretario(self):
        Secretario.objects.create(nombre="lucas_test")
        Secretario.objects.create(nombre="gaston_test")
        resp = self.client.get(reverse('app_creditos:secretario_list'))
        # import ipdb;ipdb.set_trace()
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

# las carreras deben poder crearse, obtener sus datos correctamente y relacionarse con los
# secretarios (obtener sus datos)
class CarreraTestCase(TestCase):

    def test_crear_carrera(self):
        Carrera.objects.create(nombre="ing quimica_test", años_de_duracion=5, secretario=Secretario.objects.create(
            nombre="claudio_test"))
        carrera = Carrera.objects.get(nombre="ing quimica_test")
        self.assertEqual(carrera.nombre, "ing quimica_test")
        self.assertEqual(carrera.secretario.nombre, "claudio_test")
        self.assertEqual(carrera.años_de_duracion, 5)


