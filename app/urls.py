from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    url('registrar_usuario/$', registrar_usuario, name='registrar_usuario'),
    url('listar_usuario/$', listar_usuario, name='listar_usuario'),
    url('index/$', index, name='index'),
    url(r'^$', RedirectView.as_view(url='/logar/')),
    url('logar/$', logar, name='logar'),
    url('remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario'),
    url('deslogar/$', deslogar, name='deslogar'),
]
