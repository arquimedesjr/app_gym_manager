from django import forms
from django.forms import ModelForm
from .models import Aluno, Ficha_fisica
from django.contrib.auth.models import User, Group
from django.views.generic import ListView

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'dataNascimento', 'sexo']
        sexo= (
        ('M', '1'),
        ('F', '2'),
        )
        #sexo = forms.ModelChoiceField(queryset= sexo.objects.all())

class CadastroAvaliacaoFisicaAluno(ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all())
    class Meta:
        model = Ficha_fisica
        fields = '__all__'

      