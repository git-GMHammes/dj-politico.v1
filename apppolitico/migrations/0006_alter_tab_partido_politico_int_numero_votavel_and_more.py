# Generated by Django 4.0.3 on 2022-03-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppolitico', '0005_alter_tab_2020_candidatos_dt_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='int_numero_votavel',
            field=models.CharField(default=' ', max_length=255, null=True, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='str_descricao',
            field=models.CharField(default=' ', max_length=255, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='str_partido',
            field=models.CharField(default=' ', max_length=255, null=True, verbose_name='Partido'),
        ),
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='str_sistema',
            field=models.CharField(default=' ', max_length=255, null=True, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna04',
            field=models.CharField(blank=True, default=' ', max_length=255, verbose_name='Como um AS nome CharField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna05',
            field=models.TextField(blank=True, default=' ', verbose_name='Como um AS nome TextField'),
        ),
    ]
