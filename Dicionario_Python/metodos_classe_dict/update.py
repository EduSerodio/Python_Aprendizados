# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.UPDATE - Nos permite atualizar nosso dicionário com outro dicionáriom, mas temos 
# dois cenários: se atualizarmos com uma chave já existente ele vai ser modificado 
# para os valores que passarmos na atualização, agora se passarmos outra chave, ele
# ira adicionar a chave ja existente

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 23, "telefone": "1234-5678"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "2345-8945" }}) 
print(contatos)


