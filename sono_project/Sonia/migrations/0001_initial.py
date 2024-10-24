# Generated by Django 5.1.2 on 2024-10-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_created=True, verbose_name='Data de Criação')),
                ('resultado', models.CharField(max_length=100)),
                ('imc', models.FloatField(verbose_name='IMC')),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
                ('doenca', models.BooleanField(verbose_name='Possui Doença Relevante')),
            ],
            options={
                'verbose_name': 'Dado de treino da Sonia',
                'verbose_name_plural': 'Dados de treino da Sonia',
            },
        ),
    ]
