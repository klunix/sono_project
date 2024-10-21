from django.db import models

# Create your models here.
class Problema(models.Model):
    author = models.CharField(max_length=150)
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()