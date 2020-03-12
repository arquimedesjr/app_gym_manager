from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=250, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.CharField(max_length=250, null=False)
    dataNascimento = models.CharField(max_length=250, null=False)
