from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404

from ..forms import AlunoForm
from ..models import Aluno, Ficha_fisica


def cadastrar_aluno(request, template_name='partials/alunos/aluno-form.html'):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, template_name, {
        'form': form
    })


def listar_aluno(request, template_name="partials/alunos/aluno-list.html"):
    query = request.GET.get("busca")
    if query:
        aluno = Aluno.objects.filter(modelo__icontains=query)
    else:
        aluno = Aluno.objects.all()

    paginator = Paginator(aluno, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        data = request.POST.copy()
        pkAluno = data.get('pkaluno')
        aluno = Aluno.objects.get(pk=pkAluno)
        aluno.delete()
        return redirect('aluno_list')

    alunos = {'lista': aluno, 'paginacao': page_obj}
    return render(request, template_name, alunos)


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


def remover_aluno(request, pk, template_name='partials/alunos/aluno-delete.html'):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect('aluno_list')
    return render(request, template_name, {'aluno': aluno})


def details_aluno(request, pk, template_name='partials/alunos/aluno-details.html'):
    aluno = Aluno.objects.get(pk=pk)
    return render(request, template_name, {'aluno': aluno})

def historico_avaliacao(request, pk, template_name='partials/alunos/historico-de-avaliacoes.html'):
    entrys = Ficha_fisica.objects.filter(aluno_id=pk)
    # avaliacoes = get_object_or_404(Ficha_fisica, aluno)
    return render(request, template_name, {'avaliacoes': entrys })