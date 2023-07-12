# ---------------------------------INTRODUÇÃO----------------------------------------
#Dicionários podem armazenar qualquer tipo de objeto python como valor, desde que a 
# chave para esse valor seja um objeto imutável como (strings e números)

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "eduardo@gamil.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
    "katlyn@gmail.com" : {"nome": "Katlyn", "idade": 26, "telefone": "7654-4321"},
    "gabriela@gmail.com" : {"nome": "Gabriela", "idade": 25, "telefone": "5689-7845"},
    "vanda@gmail.com" : {"nome": "Vanda", "idade": 50, "telefone": "8912-4587", "extra": {"a": 1}},
}

print(contatos)

#Para ter um acesso mais direto dentro do dicionário, fazemos da seguinte forma:
idade = contatos["eduardo@gamil.com"]["idade"]
print(idade)

#Para pegarmos o dicionário que está aninhado na chave de "vanda@gmail.com" faremos da seguinte forma:
extra = contatos["vanda@gmail.com"]["extra"]
print(extra)