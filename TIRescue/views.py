from django.shortcuts import render, redirect, get_object_or_404
from .models import Problema

# View da página inicial
def home(request):
    problemas = Problema.objects.all()
    return render(request, "tirescue/home.html", {"problemas": problemas})

# View para informar um problema
def informar_problema(request):
    if request.method == "POST":
        dados_do_problema = request.POST
        problemas = []

        # Adiciona os problemas selecionados à lista
        if dados_do_problema.get("problema_inexistencia"):
            problemas.append("non ecziste")
        if dados_do_problema.get("problema_duplicado"):
            problemas.append("doppelganger")
        if dados_do_problema.get("problema_preco"):
            problemas.append("preço")
        if dados_do_problema.get("problema_nome"):
            problemas.append("nome")
        if dados_do_problema.get("problema_marca"):
            problemas.append("marca")
        if dados_do_problema.get("problema_ncm"):
            problemas.append("CHIANCA MALDITO (NCM)")
        if dados_do_problema.get("outro_problema"):
            problemas.append(dados_do_problema.get("outro_problema"))

        # Concatena os problemas em uma string
        descricao = ", ".join(problemas)

        # Cria e salva o problema
        problema = Problema(
            author=dados_do_problema.get("author"),
            titulo=dados_do_problema.get("titulo"),
            descricao=descricao
        )
        problema.save()

        return redirect("tirescue-home")
    return render(request, "tirescue/informar_problema.html")

# View para deletar um problema
def deletar_problema(request, problema_id):
    problema = get_object_or_404(Problema, id=problema_id)
    
    if request.method == "POST":
        problema.delete()
        return redirect("tirescue-home")

    return render(request, "tirescue/confirmar_delecao.html", {"problema": problema})
