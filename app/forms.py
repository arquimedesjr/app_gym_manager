from django import forms
from django.forms import ModelForm
from .models import Aluno, Ficha_fisica

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

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

class RelatorioFisicoAluno(ModelForm):
    form = forms.ModelChoiceField(Ficha_fisica.objects.all())
    class Meta:
        model = Ficha_fisica
        fields = '__all__'
        exclude = ['aluno']


campos_choices = [
    ('medida_peito', 'Medida do peito'),
    ('medida_costas', 'Medida das costas'),
    ('medida_abdomen', 'Medida do Abdomem'),
    ('medida_triceps', 'Medida dos tríceps'),
    ('medida_biceps', 'Medida dos bíceps'),
    ('medida_antebraco', 'Medida dos Antebraços'),
    ('medida_coxa', 'Medida das coxas'),
    ('medida_panturrilha', 'Medida Panturrilha'),
]

class RelatorioFisicoAlunov2(forms.Form):
      filtros = forms.ChoiceField(choices=campos_choices, required=False)
      filtros.widget.attrs.update({'class': 'form-control'})


class FilterAluno(forms.Form):
    campoFilter = forms.CharField( label=False ,max_length=100)
    campoFilter.widget.attrs.update({'class': 'form-control', 'placeholder': 'Pesquisar aluno'})