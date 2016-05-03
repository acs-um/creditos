from django.views import generic
from django.shortcuts import redirect
from .forms import CarreraForm
from django.utils import timezone
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Carrera


class IndexView(generic.ListView):
    template_name = 'app_creditos/index.html'
    model = Carrera


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
            carrera = form.save()
            return redirect(reverse('app_creditos:index'))
    else:
        form = CarreraForm(instance=carr)
    return render(request, 'app_creditos/carrera_new.html', {'form': form})


    pass



# carrera_edit(req, 1, saludo="HOLA")