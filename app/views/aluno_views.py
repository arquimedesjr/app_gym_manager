from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import AlunoForm, RelatorioFisicoAluno, RelatorioFisicoAlunov2, FilterAluno
from ..models import Aluno, Ficha_fisica
from django.db.models import Count
from django.http import JsonResponse
from django.db import models


@login_required
def cadastrar_aluno(request, template_name='partials/alunos/aluno-form.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, template_name, { 'form': form, 'filtro': campoFiltro })

@login_required
def listar_aluno(request, template_name="partials/alunos/aluno-list.html"):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()

    if query:
        aluno = Aluno.objects.filter(nome__iexact=query)
    else:
        aluno = Aluno.objects.all()
    paginator = Paginator(aluno, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(f'Query: {query}')

    # Excluir Aluno
    if request.method == "POST":
        data = request.POST.copy()
        pkAluno = data.get('pkaluno')
        aluno = Aluno.objects.get(pk=pkAluno)
        aluno.delete()
        return redirect('aluno_list')

    return render(request, template_name, {'paginacao': page_obj, 'filtro': campoFiltro})

@login_required
def editar_aluno(request, pk, template_name='partials/alunos/aluno-edit.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, template_name, {'form': form, 'filtro': campoFiltro})

@login_required
def remover_aluno(request, pk, template_name='partials/alunos/aluno-delete.html'):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect('aluno_list')
    return render(request, template_name, {'aluno': aluno})

@login_required
def details_aluno(request, pk, template_name='partials/alunos/aluno-details.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    aluno = Aluno.objects.get(pk=pk)
    entrys = Ficha_fisica.objects.filter(aluno_id=pk).order_by('-created_at')[:5]
    form = RelatorioFisicoAluno()
    relatorio = RelatorioFisicoAlunov2()
    dados = None
    if request.method == "POST":
        data = request.POST.copy()
        campos = data.get('campos')
        dados = list(Ficha_fisica.objects.filter(aluno_id=pk).values_list(f'{campos}', flat=False))[:5]
        print(f'Filtro: {campos}')
        print(f'Dados: {dados}')
        redirect('/detalhes-aluno/{0}'.format(pk))

    return render(request, template_name,
                 {'aluno': aluno,
                  'entrys': entrys,
                  'form': form,
                  'relatorio': relatorio,
                  'dados': dados,
                  'filtro': campoFiltro
                 })

@login_required
def historico_avaliacao(request, pk, template_name='partials/alunos/historico-de-avaliacoes.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    entrys = Ficha_fisica.objects.filter(aluno_id=pk)
    count = Ficha_fisica.objects.annotate(Count('aluno_id'))
    if request.method == "POST":
        data = request.POST.copy()
        pkFicha = data.get('pkavaliacao')
        ficha = Ficha_fisica.objects.get(pk=pkFicha)
        ficha.delete()
        return redirect('/historico-de-avaliacoes/{0}'.format(pk))
    return render(request, template_name, {'avaliacoes': entrys, 'filtro': campoFiltro })

