from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import AlunoForm, RelatorioFisicoAluno
from ..models import Aluno, Ficha_fisica
from django.db.models import Count
@login_required
def cadastrar_aluno(request, template_name='partials/alunos/aluno-form.html'):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, template_name, {
        'form': form
    })

@login_required
def listar_aluno(request, template_name="partials/alunos/aluno-list.html"):
    query = request.GET.get("busca")
    if query:
        aluno = Aluno.objects.filter(modelo__icontains=query)
    else:
        aluno = Aluno.objects.all()
    paginator = Paginator(aluno, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        data = request.POST.copy()
        pkAluno = data.get('pkaluno')
        aluno = Aluno.objects.get(pk=pkAluno)
        aluno.delete()
        return redirect('aluno_list')

    return render(request, template_name, {'paginacao': page_obj})

@login_required
def editar_aluno(request, pk, template_name='partials/alunos/aluno-edit.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, template_name, {'form': form})

@login_required
def remover_aluno(request, pk, template_name='partials/alunos/aluno-delete.html'):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect('aluno_list')
    return render(request, template_name, {'aluno': aluno})

@login_required
def details_aluno(request, pk, template_name='partials/alunos/aluno-details.html'):
    aluno = Aluno.objects.get(pk=pk)
    # entrys = Ficha_fisica.objects.filter(aluno_id=pk)[:1]
    entrys = Ficha_fisica.objects.filter(aluno_id=pk)
    form = RelatorioFisicoAluno()
    if request.method == "POST":
        data = request.POST.copy()
        print(data.get('medida'))
        redirect('/detalhes-aluno/{0}'.format(pk))
    # print(entrys.medida_peso)
    return render(request, template_name,
                 {'aluno': aluno,
                  'entrys': entrys,
                  'form': form
                 })

@login_required
def historico_avaliacao(request, pk, template_name='partials/alunos/historico-de-avaliacoes.html'):
    entrys = Ficha_fisica.objects.filter(aluno_id=pk)
    count = Ficha_fisica.objects.annotate(Count('aluno_id'))
    if request.method == "POST":
        data = request.POST.copy()
        pkFicha = data.get('pkavaliacao')
        ficha = Ficha_fisica.objects.get(pk=pkFicha)
        ficha.delete()
        return redirect('/historico-de-avaliacoes/{0}'.format(pk))
    return render(request, template_name, {'avaliacoes': entrys })

