from django.core.validators import MinValueValidator
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True

    @property
    def get_created(self):
        return self.created_at.strftime("%d/%m/%Y")

    def __str__(self):
        return self.get_created

class Aluno(TimeStampMixin, models.Model):
    masculino = 'M'
    feminino = 'F' 
    tipoSexo= [
        (masculino, 'M'),
        (feminino, 'F'),
    ]
    is_fumante = [
        ('N', 'Não'),
        ('S', 'Sim')
    ]
    nome = models.CharField(max_length=250, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.CharField(max_length=250, null=False)
    dataNascimento = models.CharField(max_length=250, null=False)
    sexo = models.CharField(max_length=1, null=False, choices=tipoSexo, default= masculino)
    objetivo = models.CharField(max_length=240, null=False)
    problema_de_saude = models.CharField(max_length=350, null=False)
    ha_quanto_tempo = models.CharField(max_length=240)
    como_se_encontra = models.CharField(max_length=540)
    medicamento_utilizado = models.CharField(max_length=540)
    fumante = models.CharField(max_length=3, null=False, choices=is_fumante, default='N')
    bebida_alcoolica = models.CharField(max_length=240, null=False)
    habitos_alimentares = models.CharField(max_length=540, null=False)
    suplementos = models.CharField(max_length=540, null=False)
    idade = models.IntegerField(null=True, default="0")

    def __str__(self):
        return self.nome

class Ficha_fisica(TimeStampMixin, models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    medida_costas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_peito = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_abdomen = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_triceps_direito = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_triceps_esquerdo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_biceps_direito = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_biceps_esquerdo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_antebraco_direito = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_antebraco_esquerdo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_coxa_direita = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_coxa_esquerda = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_panturrilha_direita = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_panturrilha_esquerda = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    percentual_gordura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True )

    def __str__(self):
        return ''
    
