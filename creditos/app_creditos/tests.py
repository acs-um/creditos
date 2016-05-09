from django.test import TestCase, Client
from .models import *
'''
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
'''

# deben poder guardarse los secretarios correctamente
class SecretarioTestCase(TestCase):

    def test_crear_secretario(self):
        Secretario.objects.create(nombre="lucas_test")
        secretario = Secretario.objects.get(nombre="lucas_test")
        self.assertEqual(secretario.nombre, "lucas_test")


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


# PRUEBAS DE CLIENT
'''
class SecretarioTest(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('secretario/new/')
        data = {'nombre': 'rogrigo_test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Secretario.objects.count(), 1)
        self.assertEqual(Secretario.objects.get().name, 'rogrigo_test')
'''