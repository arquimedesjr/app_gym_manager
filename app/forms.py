from django import forms
from django.forms import ModelForm
from .models import Aluno, Ficha_fisica
from django.contrib.auth.models import User, Group

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'dataNascimento']

class CadastroAvaliacaoFisicaAluno(ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all())

    class Meta:
        model = Ficha_fisica
        fields = '__all__'

        