from django.views import generic
from django.shortcuts import redirect
from .forms import *
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import *


# CARRERAS

class IndexView(generic.ListView):
    template_name = 'app_creditos/index.html'
    model = Carrera

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        # calculo de cantidad de alumnos
        carreras = Carrera.objects.all()
        for carrera in carreras:
            carrera.cantidad_alumnos = carrera.Alumnos.count()
        context['carreras'] = carreras
        return context


def carrera_new(request):
    if request.method == "POST":
        form = CarreraForm(request.POST)
        if form.is_valid():
            carrera = form.save()
            carrera.save()
            return redirect(reverse('app_creditos:index'))
    else:
        form = CarreraForm()
    return render(request, 'app_creditos/carrera_new.html', {'form': form})


def carrera_edit(request, pk):
    carr = Carrera.objects.get(pk=pk)

    if request.method == "POST":
        form = CarreraForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:index'))
    else:
        form = CarreraForm(instance=carr)
    return render(request, 'app_creditos/carrera_new.html', {'form': form})


def carrera_delete(request, pk):
    Carrera.objects.get(pk=pk).delete()
    return redirect(reverse('app_creditos:index'))


def carrera_disable(request, pk):
    carr = Carrera.objects.get(pk=pk)
    carr.estado = False
    carr.save()
    return redirect(reverse('app_creditos:index'))


# ALUMNOS

class AlumnoView(generic.ListView):
    template_name = 'app_creditos/alumno_list.html'
    model = Alumno


def alumno_new(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            alumno.save()
            return redirect(reverse('app_creditos:alumno_list'))
    else:
        form = AlumnoForm()
    return render(request, 'app_creditos/alumno_new.html', {'form': form})


def alumno_edit(request, pk):
    carr = Alumno.objects.get(pk=pk)

    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:alumno_list'))
    else:
        form = AlumnoForm(instance=carr)
    return render(request, 'app_creditos/alumno_new.html', {'form': form})


def alumno_delete(request, pk):
    Alumno.objects.get(pk=pk).delete()
    return redirect(reverse('app_creditos:alumno_list'))


def alumno_disable(request, pk):
    carr = Alumno.objects.get(pk=pk)
    carr.estado = False
    carr.save()
    return redirect(reverse('app_creditos:alumno_list'))


# SECRETARIOS

class SecretarioView(generic.ListView):
    template_name = 'app_creditos/secretario_list.html'
    # model = Secretario

    def get_queryset(self):
        return Secretario.objects.filter(estado=True)


def secretario_new(request):
    if request.method == "POST":
        form = SecretarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:secretario_list'))
    else:
        form = SecretarioForm()
    return render(request, 'app_creditos/secretario_new.html', {'form': form})


def secretario_edit(request, pk):
    carr = Secretario.objects.get(pk=pk)

    if request.method == "POST":
        form = SecretarioForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:secretario_list'))
    else:
        form = SecretarioForm(instance=carr)
    return render(request, 'app_creditos/secretario_new.html', {'form': form})


def secretario_delete(request, pk):
    Secretario.objects.get(pk=pk).delete()
    return redirect(reverse('app_creditos:secretario_list'))


def secretario_disable(request, pk):
    carr = Secretario.objects.get(pk=pk)
    carr.estado = False
    carr.save()
    return redirect(reverse('app_creditos:secretario_list'))


# MATERIAS

class MateriaView(generic.ListView):
    template_name = 'app_creditos/materia_list.html'
    model = Materia


def materia_new(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:materia_list'))
    else:
        form = MateriaForm()
    return render(request, 'app_creditos/materia_new.html', {'form': form})


def materia_edit(request, pk):
    carr = Materia.objects.get(pk=pk)

    if request.method == "POST":
        form = MateriaForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_creditos:materia_list'))
    else:
        form = MateriaForm(instance=carr)
    return render(request, 'app_creditos/materia_new.html', {'form': form})


def materia_delete(request, pk):
    Materia.objects.get(pk=pk).delete()
    return redirect(reverse('app_creditos:materia_list'))


def materia_detail(request, pk):
    materia = Materia.objects.get(pk=pk)
    correlativas = materia.correlativas.all()

    return render(request, 'app_creditos/materia_detail.html', {'correlativas': correlativas,
                                                                'materia': materia})


def materia_disable(request, pk):
    carr = Materia.objects.get(pk=pk)
    carr.estado = False
    carr.save()
    return redirect(reverse('app_creditos:materia_list'))