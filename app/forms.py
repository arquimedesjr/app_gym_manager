from django import forms
from django.forms import ModelForm
from .models import Aluno, Ficha_fisica

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'dataNascimento', 'sexo']
       
        #sexo = forms.ModelChoiceField(queryset= sexo.objects.all())

class CadastroAvaliacaoFisicaAluno(ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all())
    class Meta:
        model = Ficha_fisica
        fields = '__all__'

class EditarFichaMedicaAluno(ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all())
    class Meta:
        model = Ficha_fisica
        fields = '__all__'        

      