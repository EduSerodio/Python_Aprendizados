# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.GET  - É uma das formas de acessar valores dentro de um dicionário.

# -----------------------------------Exemplos------------------------------------------
contatos = {"eduardo@gmail.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"}}

# KeyError
#contatos["chave"]

#quando nao sabemos se a chave existe ou não no dicionário usamos dessa forma:
teste = contatos.get("chave")
print(teste)

#aqui passamos uma chave como parâmetro do get, e se ele não encontrar ele retorna um dict vazio
teste2 = contatos.get("chave", {})
print(teste2)

#nesse teste é o mesmo caso do de cima, mas passando uma chave existente
teste3 = contatos.get(
    "eduardo@gmail.com", {}
)
print(teste3)