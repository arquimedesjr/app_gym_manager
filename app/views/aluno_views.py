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
    paginator = Paginator(aluno, 8)
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
    
    entrys = Ficha_fisica.objects.all().filter(aluno_id=pk).values().order_by('created_at')[:5]

    relatorio = RelatorioFisicoAlunov2()
    print(f'Entrys: {entrys}')

    # Filtro de dados
    if request.method == "POST":
        data = request.POST.copy()
        campos = data.get('campos')
        # entrys = Ficha_fisica.objects.all().filter(aluno_id=pk).values(f'{campos}').order_by('created_at')[:5]
        redirect('/detalhes-aluno/{0}'.format(pk))

    # Charts Peso
    peso = Ficha_fisica.objects.filter(aluno_id=pk).order_by('created_at')[:5]

    # Charts Peso
    percentual_de_gordura = Ficha_fisica.objects.filter(aluno_id=pk).order_by('created_at')[:5]

    return render(request, template_name,
                 {'aluno': aluno,
                  'entrys': entrys,
                  'relatorio': relatorio,
                  'filtro': campoFiltro,
                  'peso': peso,
                  'percentual_de_gordura': percentual_de_gordura
                 })

@login_required
def historico_avaliacao(request, pk, template_name='partials/alunos/historico-de-avaliacoes.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')
    aluno = Aluno.objects.filter(pk=pk).values('nome')
    entrys = Ficha_fisica.objects.filter(aluno_id=pk)
    count = Ficha_fisica.objects.filter(aluno_id=pk).count()
    print(f'Dados do aluno: {aluno}')
    if request.method == "POST":
        data = request.POST.copy()
        pkFicha = data.get('pkavaliacao')
        ficha = Ficha_fisica.objects.get(pk=pkFicha)
        ficha.delete()
        return redirect('/historico-de-avaliacoes/{0}'.format(pk))
    return render(request, template_name, {'avaliacoes': entrys, 'filtro': campoFiltro, 'aluno': aluno })

@login_required
def details_avaliacao(request, pk, template_name='partials/alunos/avaliacao-detail.html'):
    # Filtrar Aluno
    query = request.GET.get("campoFilter")
    campoFiltro = FilterAluno()
    if query:
        return redirect(f'/listar-aluno/?campoFilter={query}')

    aluno = Aluno.objects.filter(pk=pk).values('nome')
    entrys = Ficha_fisica.objects.filter(id=pk)
    print(f'Dados do aluno: {aluno}')

    return render(request, template_name, {'avaliacoes': entrys, 'filtro': campoFiltro, 'aluno': aluno })

