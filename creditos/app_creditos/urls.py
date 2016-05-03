from django.conf.urls import url
from . import views

app_name = 'app_creditos'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^carrera/new/$', views.carrera_new, name='carrera_new'),
    url(r'^carrera/(?P<pk>\d+)/$', views.carrera_edit, name='carrera_edit'),
]
