from django.db import models

# Create your models here.
# ↓ Antes: python manage.py migrate
from django.db import models
# ↓ Acrescentar esta importação
from django.utils import timezone

# Create your models here.


class Tab_tipos(models.Model):
    coluna01 = models.BooleanField(
        blank=False,
        default=True, verbose_name='Como um AS nome BooleanField')
    coluna02 = models.IntegerField(
        default=0, blank=True, verbose_name='Como um AS nome IntegerField')
    coluna03 = models.DecimalField(
        blank=True,
        max_digits=11, decimal_places=10, verbose_name='Como um AS nome DecimalField')
    coluna04 = models.CharField(
        blank=True,
        default=' ', max_length=255, verbose_name='Como um AS nome CharField')
    coluna05 = models.TextField(
        blank=True, default=' ', verbose_name='Como um AS nome TextField')
    coluna06 = models.ImageField(
        blank=True, verbose_name='Como um AS nome ImageField')
    coluna07 = models.FloatField(
        blank=True, default=0, verbose_name='Como um AS nome FloatField')
    coluna08 = models.DateTimeField(
        blank=True,
        default=timezone.now, verbose_name='Como um AS nome DateTimeField')


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
    dt_geracao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Data')
    tm_geracao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Hora')
    int_ano_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Ano')
    int_tipo_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='TipoN')
    str_tipo_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='TipoC')
    int_turno = models.CharField(
        null=True, default='', max_length=255, verbose_name='Turno')
    int_cod_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Cod')
    str_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Eleições')
    dt_eleicao = models.CharField(
        null=True, default='', max_length=255, verbose_name='Data')
    str_tipo_abrangencia = models.CharField(
        null=True, default='', max_length=255, verbose_name='Abrangência')
    str_sigla_uf = models.CharField(
        null=True, default='', max_length=255, verbose_name='UF')
    str_sigla_uf = models.CharField(
        null=True, default='', max_length=255, verbose_name='UF')
    str_sigla_unidade_eleitoral = models.CharField(
        null=True, default='', max_length=255, verbose_name='Unidade')
    str_nome_unidade_eleitoral = models.CharField(
        null=True, default='', max_length=255, verbose_name='Unidade')
    int_cod_cargo = models.CharField(
        null=True, default='', max_length=255, verbose_name='Cod')
    str_desc_cargo = models.CharField(
        null=True, default='', max_length=255, verbose_name='Cargo')
    str_partido_politico = models.CharField(
        null=True, default='', max_length=255, verbose_name='Partido 1')
    key_partido = models.ForeignKey(
        Tab_partido_politico, blank=False, default='00', on_delete=models.DO_NOTHING, verbose_name='Partido 2')
    int_numero_votavel = models.CharField(
        null=True, default='', max_length=255, verbose_name='Nº')
    str_nome_votavel = models.CharField(
        null=True, default='', max_length=255, verbose_name='Nome')
    str_nome_social = models.CharField(
        null=True, default='', max_length=255, blank=False, verbose_name='Político')
    str_vice_suplente = models.CharField(
        null=True, default='', max_length=255, blank=False, verbose_name='Vice')
    int_qtd_votos = models.CharField(
        null=True, default='', max_length=255, verbose_name='Votos')
    str_situacao = models.CharField(
        null=True, default='', max_length=255, blank=False, verbose_name='Situação')
    str_onde = models.CharField(
        null=True, default='', max_length=255, blank=False, verbose_name='Onde')
    dt_criacao = models.DateTimeField(
        null=True, default=timezone.now, verbose_name='Criação')
    str_sistema = models.CharField(
        null=True, default='', max_length=255, blank=False, verbose_name='Situação')

    def __str__(self):
        return self.str_nome_votavel