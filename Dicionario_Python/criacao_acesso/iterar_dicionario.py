# ---------------------------------INTRODUÇÃO----------------------------------------
# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando
# for.

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "eduardo@gamil.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
    "katlyn@gmail.com" : {"nome": "Katlyn", "idade": 26, "telefone": "7654-4321"},
    "gabriela@gmail.com" : {"nome": "Gabriela", "idade": 25, "telefone": "5689-7845"},
    "vanda@gmail.com" : {"nome": "Vanda", "idade": 50, "telefone": "8912-4587", "extra": {"a": 1}},
}

# primeira forma mas não muito recomendada de se percorrer um dicionário:

for chave in contatos:
    print(chave, contatos[chave])

# Segunda forma e mais recomendada, é ultilizando o método .items() junto com o for:

for chave, valor in contatos.items():
    print(chave, valor)