# Generated by Django 4.2.11 on 2024-09-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recomendar', '0002_dadosdepessoasmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosdepessoasmodel',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
