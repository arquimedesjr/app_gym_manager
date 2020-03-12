from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    #Login 
    url(r'^$', RedirectView.as_view(url='/logar/')),
    url('logar/$', logar, name='logar'),
    url('deslogar/$', deslogar, name='deslogar'),
    url('esqueci-minha-senha/$', esqueci_minha_senha, name="esqueci_minha_senha"),
    
    # Index Dashboard
    url('index/$', index, name='index'),

    # aluno
    url('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    url(r'^listar_aluno/', listar_aluno, name='aluno_list'),
    url(r'^editar_aluno/(?P<pk>[0-9]+)', editar_aluno, name='editar_aluno'),
    url(r'^remover_aluno/(?P<pk>[0-9]+)', remover_aluno, name='remover_aluno'),

    # não definido
    url('registrar_usuario/$', registrar_usuario, name='registrar_usuario'),
    url('listar_usuario/$', listar_usuario, name='listar_usuario'),
    url('remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario')

]
