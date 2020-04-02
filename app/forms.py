from django.forms import ModelForm
from .models import Aluno, Ficha_fisica


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'dataNascimento']

class CadastroAvaliacaoFisicaAluno(ModelForm):
    class Meta:
        model = Ficha_fisica
        fields = ['medida_costas', 'medida_peito', 'medida_abdome', 'medida_tricpes', 'medida_biceps', 'medida_antibraco', 'medida_coxa', 'medida_panturrilha', 'medida_peso']