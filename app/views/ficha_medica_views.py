from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import AlunoForm, CadastroAvaliacaoFisicaAluno, EditarFichaMedicaAluno, FilterAluno
from ..models import Aluno, Ficha_fisica

@login_required
def cadastrar_avaliacao_fisica(request, template_name='partials/alunos/add-avaliacao-fisica.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    form = CadastroAvaliacaoFisicaAluno(request.POST)

    if request.method == "POST":
        if form.is_valid():
            data = request.POST.copy()
            aluno_id = data.get('aluno')
            form.save()
            return redirect(f'/historico-de-avaliacoes/{aluno_id}')
        else: 
            messages.error(request, 'Dados incorretos. Tente novamente')
            return redirect('cadastrar_avaliacao_fisica')
    return render(request, template_name, {'form': form, 'filtro': campoFiltro })

@login_required
def editar_avaliacao(request, pk, template_name='partials/alunos/edit-avaliacao-fisica.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')
    
    idficha = Ficha_fisica.objects.get(pk=pk)
    if request.method == "POST":
        form =  EditarFichaMedicaAluno(request.POST, instance=idficha)
        if form.is_valid():
            form.save()
            redirect('/editar-avaliacao/{0}'.format(pk))
        else:
            messages.error(request, 'Os dados foram inseridos de forma incorreta.')
            redirect('/editar-avaliacao/{0}'.format(pk))
    else: 
        form =  EditarFichaMedicaAluno(instance=idficha)
    # form = Ficha_fisica.object.get(pk=pk)
    return render(request, template_name, {'form': form, 'filtro': campoFiltro })