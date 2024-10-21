from django.shortcuts import render
from .forms import FormularioRecomendacaoForm
from .models import DadosDePessoasModel

# Create your views here.
def formularioRecomendacao(request):
    if request.method == "POST":
        form = FormularioRecomendacaoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Aqui você deve passar os campos corretamente, usando o dicionário `data`
            dadosdepessoal = DadosDePessoasModel(
                nome=data['nome'],
                telefone=data['telefone'],
                email=data['email'],
                altura=data['altura'],
                idade=data['idade'],
                modelo_anterior=data['modelo_anterior'],
                quantos_acompanhantes=data['quantos_acompanhantes'],
                tem_doenca=data['tem_doenca'],
                peso=data['peso']
            )
            
            dadosdepessoal.save()
            
            return render(request, "recomendar/listar_recomendacoes.html")
        
    return render(request, "recomendar/formulario_cliente.html")


def listarTreino(request):
    pass

def adicionarTreino(request):
    if request.method == "POST":
        pass
    
    return render(request, "recomendar/formulario_cliente.html")