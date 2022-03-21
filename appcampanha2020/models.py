from django.db import models

# Create your models here.
# ↓ Antes: python manage.py migrate
from django.db import models
# ↓ Acrescentar esta importação
from django.utils import timezone

# Create your models here.

class Tab_partido_politico(models.Model):
    str_partido = models.CharField(
        null=True, default=' ', max_length=255, verbose_name='Partido')
    int_numero_votavel = models.CharField(
        null=True, default=' ', max_length=255, verbose_name='Numero')
    str_descricao = models.CharField(
        null=True, default=' ', max_length=255, verbose_name='Descrição')
    dt_criacao = models.DateTimeField(
        null=timezone.now, verbose_name='Criação')
    str_sistema = models.CharField(
        null=True, default=' ', max_length=255, verbose_name='Situação')

    def __str__(self):
        return self.str_partido

class Tab_2020_candidato(models.Model):
    pass

class Tab_campanha2018(models.Model):
    pass

