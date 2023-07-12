# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.IN - É uma outra forma mais "ELEGANTE" para verificarmos se uma chave ela existe
# ou não dentro de um dicionário

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "eduardo@gamil.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
    "katlyn@gmail.com" : {"nome": "Katlyn", "idade": 26, "telefone": "7654-4321"},
    "gabriela@gmail.com" : {"nome": "Gabriela", "idade": 25, "telefone": "5689-7845"},
    "vanda@gmail.com" : {"nome": "Vanda", "idade": 50, "telefone": "8912-4587", "extra": {"a": 1}},
}

resultado = "eduardo@gamil.com" in contatos
print(resultado)

resultado2 = "robson@gmail.com" in contatos
print(resultado2)

resultado3 = "idade" in contatos["gabriela@gmail.com"]
print(resultado3)

resultado4 = "telefone" in contatos["vanda@gmail.com"]
print(resultado4)