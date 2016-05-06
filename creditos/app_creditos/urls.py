from django.conf.urls import url
from . import views

app_name = 'app_creditos'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ABM carreras
    url(r'^carrera/new/$', views.carrera_new, name='carrera_new'),
    url(r'^carrera/(?P<pk>\d+)/$', views.carrera_edit, name='carrera_edit'),
    url(r'^carrera/delete/(?P<pk>\d+)/$', views.carrera_delete, name='carrera_delete'),
    url(r'^carrera/disable/(?P<pk>\d+)/$', views.carrera_disable, name='carrera_disable'),

    # ABM alumnos
    url(r'^alumno/new/$', views.alumno_new, name='alumno_new'),
    url(r'^alumno/list/$', views.AlumnoView.as_view(), name='alumno_list'),
    url(r'^alumno/(?P<pk>\d+)/$', views.alumno_edit, name='alumno_edit'),
    url(r'^alumno/delete/(?P<pk>\d+)/$', views.alumno_delete, name='alumno_delete'),
    url(r'^alumno/disable/(?P<pk>\d+)/$', views.alumno_disable, name='alumno_disable'),

    # ABM secretarios
    url(r'^secretario/new/$', views.secretario_new, name='secretario_new'),
    url(r'^secretario/list/$', views.SecretarioView.as_view(), name='secretario_list'),
    url(r'^secretario/(?P<pk>\d+)/$', views.secretario_edit, name='secretario_edit'),
    url(r'^secretario/delete/(?P<pk>\d+)/$', views.secretario_delete, name='secretario_delete'),
    url(r'^secretario/disable/(?P<pk>\d+)/$', views.secretario_disable, name='secretario_disable'),

    # ABM materias
    url(r'^materia/new/$', views.materia_new, name='materia_new'),
    url(r'^materia/list/$', views.MateriaView.as_view(), name='materia_list'),
    url(r'^materia/(?P<pk>\d+)/$', views.materia_edit, name='materia_edit'),
    url(r'^materia/delete/(?P<pk>\d+)/$', views.materia_delete, name='materia_delete'),
    url(r'^materia/detail/(?P<pk>\d+)/$', views.materia_detail, name='materia_detail'),

]
