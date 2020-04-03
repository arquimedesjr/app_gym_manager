from django.forms import ModelForm
from .models import Aluno, Ficha_fisica


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'dataNascimento']

class CadastroAvaliacaoFisicaAluno(ModelForm):
    class Meta:
        model = Ficha_fisica
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(CadastroAvaliacaoFisicaAluno, self).__init__(*args, **kwargs)
    #     self.fields['medida_costas'].widget.attrs.update({'class' : 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super(CadastroAvaliacaoFisicaAluno, self).__init__(*args, **kwargs)
    #     for field in self.fields: 
    #         field.widget.attrs.update({'class': 'form-control'})