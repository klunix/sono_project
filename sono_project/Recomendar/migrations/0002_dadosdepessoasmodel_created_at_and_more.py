# Generated by Django 4.2.11 on 2024-09-19 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Recomendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosdepessoasmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadosdepessoasmodel',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='dadosdepessoasmodel',
            name='quantos_acompanhantes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadosdepessoasmodel',
            name='telefone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='dadosdepessoasmodel',
            name='peso',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='dadosdepessoasmodel',
            name='tem_doenca',
            field=models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1),
            preserve_default=False,
        ),
    ]
