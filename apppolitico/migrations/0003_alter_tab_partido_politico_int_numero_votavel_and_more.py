# Generated by Django 4.0.3 on 2022-03-19 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apppolitico', '0002_alter_tab_2020_candidatos_key_partido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='int_numero_votavel',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='str_descricao',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tab_partido_politico',
            name='str_partido',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Partido'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna02',
            field=models.IntegerField(blank=True, default=0, verbose_name='Como um AS nome IntegerField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna03',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=11, verbose_name='Como um AS nome DecimalField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna04',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Como um AS nome CharField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna05',
            field=models.TextField(blank=True, default='', verbose_name='Como um AS nome TextField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna06',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Como um AS nome ImageField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna07',
            field=models.FloatField(blank=True, default=0, verbose_name='Como um AS nome FloatField'),
        ),
        migrations.AlterField(
            model_name='tab_tipos',
            name='coluna08',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Como um AS nome DateTimeField'),
        ),
    ]
