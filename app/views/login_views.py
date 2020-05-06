from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum
from ..models import Aluno, Ficha_fisica
from ..forms import FilterAluno
from django.db.models.expressions import datetime
# Create your views here.
@login_required
def registrar_usuario(request, template_name="registrar.html"):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        tipo = request.POST['tipo_usuario']

        try:
            if tipo == "administrador":
                user = User.objects.create_user(username, email, password)
                user.is_staff = True
                user.save()
            else:
                user = User.objects.create_user(username, email, password)
        except:
            messages.error(request, 'Erro ao preenchimento')

        return redirect('/app/listar_usuario/')
    else:
        return render(request, template_name, {'filtro': campoFiltro})


@login_required
def listar_usuario(request, template_name="listar.html"):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    usuarios = User.objects.all()
    usuario = {'lista': usuarios, 'filtro': campoFiltro}
    return render(request, template_name, usuario)


def logar(request, template_name="login.html"):
    next = request.GET.get('next', '/index/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)

        else:
            messages.error(request, 'Usuário ou senha informadas, estão incorretas.')
            return redirect('logar')

    return render(request, template_name, {'redirect_to': next})


@login_required
def remover_usuario(request, pk, template_name='delete.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    user = request.user
    if user.has_perm('user.delete_user'):
        try:
            usuario = User.objects.get(pk=pk)
            if request.method == "POST":
                usuario.delete()
                return redirect('listar_usuario')
        except:
            messages.error(request, 'Usuário não encontrado.')
            return redirect('/app/listar_usuario/')
    else:
        messages.error(request, 'Permissão negada.')
        return redirect('/app/listar_usuario/')

    return render(request, template_name, {'usuario': usuario})


@login_required
def index(request, template_name='dashboard-adm.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    # insights
    aluno = Aluno.objects.count()
    fichas = Ficha_fisica.objects.count()
    sem_ficha = Aluno.objects.filter(id__in=Ficha_fisica.objects.values('aluno_id')).count()    

    # gráficos
    charts_aluno = Aluno.objects.filter().values('created_at__date').order_by('created_at__date').annotate(count=Count('id'))
    charts_avaliacao = Ficha_fisica.objects.filter().values('created_at__date').order_by('created_at__date').annotate(count=Count('id'))

    dias = Ficha_fisica.objects.filter().extra({'date_created' : "date(created_at)"}).values('created_at').annotate(created_count=Count('id'))

    return render(request, template_name, 
                    { 'aluno' : aluno,
                      'fichas' : fichas,
                      'filtro': campoFiltro,
                      'sem_ficha': sem_ficha,
                      'charts_aluno':charts_aluno,
                      'charts_avaliacao': charts_avaliacao
                     })


def deslogar(request):
    logout(request)
    return redirect('logar')


def esqueci_minha_senha(request):
    return render(request, 'esqueci-minha-senha.html')


def resetar_senha(request, template_name='registration/password_reset_form.html'):
    return render(request, template_name)
