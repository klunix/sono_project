from django.db import models

# Create your models here.
class DadosDePessoasModel(models.Model):
    TIPO_DO_MODELO = [
        ("NS", "Não Sabe"),
        ("EF", "Extra Firme"),
        ("F", "Firme"),
        ("I", "Intermediário"),
        ("M", "Macio")
    ]

    DOENCA_CHOICES = [
        ("S", "Sim"),
        ("N", "Não")
    ]

    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=13, null=True)
    email =  models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    idade = models.IntegerField()
    altura = models.IntegerField()
    modelo_anterior = models.CharField(
        max_length=2,
        choices=TIPO_DO_MODELO
    )
    quantos_acompanhantes = models.IntegerField()
    tem_doenca = models.CharField(
        max_length=1,
        choices=DOENCA_CHOICES,
        blank=True,
    )

    peso = models.CharField(max_length=80)

    def __str__(self):
        return self.nome + " | " + str(self.created_at)


class ModeloDeColchoes(models.Model):
    TIPO_DO_MODELO = [
        ("EF", "Extra Firme"),
        ("F", "Firme"),
        ("I", "Intermediário"),
        ("M", "Macio")
    ]
    nome = models.CharField(max_length=100)
    nivel_de_maciez = models.IntegerField()
    categoria = models.CharField(
        max_length=60,
        choices=TIPO_DO_MODELO
    )