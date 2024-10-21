from django import forms

class FormularioRecomendacaoForm(forms.Form):
    nome = forms.CharField(label="Qual é o seu nome?")
    telefone = forms.CharField(max_length=13, required=False)
    email = forms.CharField(required=False)
    
    idade = forms.IntegerField()
    altura = forms.IntegerField()
    modelo_anterior = forms.ChoiceField(
        choices=[
            ("NS", "Não Sabe"),
            ("EF", "Extra Firme"),
            ("F", "Firme"),
            ("I", "Intermediário"),
            ("M", "Macio")
        ], 
        label="Qual tipo de colchão você usava?"
    )

    quantos_acompanhantes = forms.IntegerField(min_value=0)
    
    tem_doenca = forms.ChoiceField(
        choices=[
            ("S","Sim"),
            ("N","Não")
        ],
        label="Você tem alguma doença de coluna?", 
    )

    peso = forms.CharField(required=True)