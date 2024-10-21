import random
from faker import Faker

def criar_pessoa_falsa():
    fake = Faker('pt_BR')

    # Gera dados básicos
    nome = fake.name()
    endereco = fake.address()
    email = fake.email()
    telefone = fake.phone_number()

    # Gera altura entre 1.50m e 2.00m
    altura = round(random.uniform(1.50, 2.00), 2)

    # Gera peso entre 50kg e 120kg
    peso = round(random.uniform(50, 120), 1)

    # Simula se a pessoa tem problema na coluna ou não
    problemas_coluna = random.choice([True, False])

    pessoa = {
        'nome': nome,
        'endereco': endereco,
        'email': email,
        'telefone': telefone,
        'altura': altura,
        'peso': peso,
        'problemas_coluna': problemas_coluna
    }

    return pessoa

pessoa_falsa = criar_pessoa_falsa()
print(pessoa_falsa)
