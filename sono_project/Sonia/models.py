from django.db import models

# Create your models here.
class Treino(models.Model):

    resultado = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(verbose_name="Data de Criação",auto_created=True)
    imc = models.FloatField(verbose_name="IMC")
    altura = models.FloatField()
    peso = models.FloatField()
    doenca = models.BooleanField(verbose_name="Possui Doença Relevante")

    class Meta:
        verbose_name = "Dado de treino da Sonia"
        verbose_name_plural = "Dados de treino da Sonia"

    def __str__(self):
        return self.name
