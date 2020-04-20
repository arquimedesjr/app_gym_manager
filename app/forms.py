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

class RelatorioFisicoAluno(ModelForm):
    form = forms.ModelChoiceField(Ficha_fisica.objects.all())
    class Meta:
        model = Ficha_fisica
        fields = '__all__'
        exclude = ['aluno']


campos_choices = [
    ('medida_peito', 'Medida do peito'),
    ('medida_costas', 'Medida das costas'),
    ('medida_abdome', 'Medida do Abdomem'),
    ('medida_tricpes', 'Medida dos tríceps'),
    ('medida_biceps', 'Medida dos bíceps'),
    ('medida_antibraco', 'Medida dos Antebraços'),
    ('medida_coxa', 'Medida das coxas'),
    ('medida_panturrilha', 'Medida Panturrilha'),
    ('medida_peso', 'Peso'),
    ('percentual_gordura', 'Percentual de Gordura')
]

class RelatorioFisicoAlunov2(forms.Form):
      campos = forms.ChoiceField(choices=campos_choices, required=False)
      campos.widget.attrs.update({'class': 'form-control'})