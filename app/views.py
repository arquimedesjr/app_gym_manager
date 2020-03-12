from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
@login_required
def registrar_usuario(request, template_name="registrar.html"):
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
        return render(request, template_name)


@login_required
def listar_usuario(request, template_name="listar.html"):
    usuarios = User.objects.all()
    usuario = {'lista': usuarios}
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
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, template_name, {'redirect_to': next})


@login_required
def remover_usuario(request, pk, template_name='delete.html'):
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
    return render(request, template_name)

def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def esqueci_minha_senha(request):
    return render(request, 'esqueci-minha-senha.html')


def cadastrar_aluno(request, template_name='partials/alunos/aluno-form.html'):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, template_name,{
                            'form': form
                            })

def listar_aluno(request, template_name="partials/alunos/aluno-list.html"):
    query = request.GET.get("busca")
    if query:
        aluno = Aluno.objects.filter(modelo__icontains=query)
    else:
        aluno = Aluno.objects.all()
    alunos = {'lista': aluno}
    return render(request, template_name, alunos)


def editar_aluno(request, pk, template_name='partials/alunos/aluno-form.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, template_name, {'form': form})


def remover_aluno(request, pk, template_name='partials/alunos/aluno-delete.html'):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect('aluno_list')
    return render(request, template_name, {'aluno': aluno})


def resetar_senha(request, template_name='registration/password_reset_form.html'):
    return render(request, template_name)