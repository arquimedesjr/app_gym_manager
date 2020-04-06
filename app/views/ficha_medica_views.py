from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from ..forms import AlunoForm, CadastroAvaliacaoFisicaAluno
from ..models import Aluno

def cadastrar_avaliacao_fisica(request, template_name='partials/alunos/add-avaliacao-fisica.html'):
    # aluno = get_object_or_404(Aluno, pk=pk)
    form = CadastroAvaliacaoFisicaAluno(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            redirect('aluno_list')
        else: 
            messages.error(request, 'Dados incorretos. Tente novamente')
            return redirect(template_name)
    return render(request, template_name, {'form': form })