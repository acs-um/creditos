from django.views import generic
from .models import Carrera


class IndexView(generic.ListView):
    template_name = 'app_creditos/index.html'
    model = Carrera
