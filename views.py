from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def registrar_usuario(request, template_name="registrar.html"):
    user = request.user
    if user.is_staff:
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

            return redirect('/listar_usuario/')
        else:
            messages.error(request, 'Permissão negada.')
            return redirect('/listar_usuario/')
    else:
        return render(request, template_name)
    return render(request, template_name, {})


@login_required
def listar_usuario(request, template_name="listar.html"):
    usuarios = User.objects.all()
    usuario = {'lista': usuarios}
    return render(request, template_name, usuario)


def logar(request, template_name="login.html"):
    next = request.GET.get('next', '/listar_usuario/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
            messages.error(request, 'Usuário ou senha incorretos.')
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
            return redirect('/listar_usuario/')
    else:
        messages.error(request, 'Permissão negada.')
        return redirect('/listar_usuario/')

    return render(request, template_name, {'usuario': usuario})


def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
