from django.views.generic import View

from django.shortcuts import render
from .models import Treino
from . import utils


class ListarTreinamento(View):
    def get(self, request):
        treinos = Treino.objects.all()
        return render(request, "sonia/treinamento/index.html", {"treinos":treinos})
    
class CriarTreinamento(View):
    def get(self, request):
        return render(request, "sonia/treinamento/create.html")
