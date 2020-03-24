from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    #Login 
    url(r'^$', RedirectView.as_view(url='/logar/')),
    url('logar/$', logar, name='logar'),
    url('deslogar/$', deslogar, name='deslogar'),
    url('esqueci-minha-senha/$', esqueci_minha_senha, name="esqueci-minha-senha"),
    
    # Index Dashboard
    url('index/$', index, name='index'),

    # aluno
    url('cadastrar-aluno/', cadastrar_aluno, name='cadastrar-aluno'),
    url(r'^listar-aluno/', listar_aluno, name='aluno-list'),
    url(r'^editar-aluno/(?P<pk>[0-9]+)', editar_aluno, name='editar-aluno'),
    url(r'^remover-aluno/(?P<pk>[0-9]+)', remover_aluno, name='remover-aluno'),

    # não definido
    url('registrar-usuario/$', registrar_usuario, name='registrar-usuario'),
    url('listar-usuario/$', listar_usuario, name='listar-usuario'),
    url('remover-usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover-usuario')

]
