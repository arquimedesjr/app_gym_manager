from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import AlunoForm, CadastroAvaliacaoFisicaAluno, EditarFichaMedicaAluno
from ..models import Aluno, Ficha_fisica

@login_required
def cadastrar_avaliacao_fisica(request, template_name='partials/alunos/add-avaliacao-fisica.html'):
    # aluno = get_object_or_404(Aluno, pk=pk)
    form = CadastroAvaliacaoFisicaAluno(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            redirect('aluno_list')
        else: 
            messages.error(request, 'Dados incorretos. Tente novamente')
            return redirect('cadastrar_avaliacao_fisica')
    return render(request, template_name, {'form': form })

@login_required
def editar_avaliacao(request, pk, template_name='partials/alunos/edit-avaliacao-fisica.html'):
    form =  EditarFichaMedicaAluno(request.POST)
    idficha = Ficha_fisica.objects.get(pk=pk)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            redirect('/editar-avaliacao/{0}'.format(pk))
        else:
            messages.error(request, 'Os dados foram inseridos de forma incorreta.')
            redirect('/editar-avaliacao/{0}'.format(pk))
    # form = Ficha_fisica.object.get(pk=pk)
    return render(request, template_name, {'form': form })