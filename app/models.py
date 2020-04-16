from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.from django.db import models
class Aluno(models.Model):
    masculino = 'M'
    feminino = 'F' 
    tipoSexo= [
        (masculino, 'M'),
        (feminino, 'F'),
    ]
    nome = models.CharField(max_length=250, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.CharField(max_length=250, null=False)
    dataNascimento = models.CharField(max_length=250, null=False)
<<<<<<< HEAD
    sexo = models.CharField(max_length=1, null=False, choices=tipoSexo, default= masculino)
=======
    sexo = models.CharField(max_length=1, null=False, choices=tipoSexo)
   
>>>>>>> 93f6f2a8e4811c0e51f930a5d35fadf55f1bcb8d

    def __str__(self):
        return self.nome

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True

    @property
    def get_created(self):
        return self.created_at.strftime("%m/%d/%Y")

    def __str__(self):
        return self.get_created
    

class Ficha_fisica(TimeStampMixin, models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    medida_costas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_peito = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_abdome = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_tricpes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_biceps = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_antibraco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_coxa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_panturrilha = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medida_peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    percentual_gordura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return ''
    
