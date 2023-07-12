# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.CLEAR - Apaga todos os valores existente no dicionário selecionado

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "eduardo@gamil.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
    "katlyn@gmail.com" : {"nome": "Katlyn", "idade": 26, "telefone": "7654-4321"},
    "gabriela@gmail.com" : {"nome": "Gabriela", "idade": 25, "telefone": "5689-7845"},
    "vanda@gmail.com" : {"nome": "Vanda", "idade": 50, "telefone": "8912-4587", "extra": {"a": 1}},
}

contatos.clear()
print(contatos)
