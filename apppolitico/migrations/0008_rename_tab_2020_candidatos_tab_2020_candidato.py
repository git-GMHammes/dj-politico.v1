# Generated by Django 4.0.3 on 2022-03-19 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppolitico', '0007_tab_2020_candidatos_str_nome_unidade_eleitoral'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tab_2020_candidatos',
            new_name='Tab_2020_candidato',
        ),
    ]
