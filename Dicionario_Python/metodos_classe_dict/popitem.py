# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.POPITEM - Serve para remover tamém, mas a diferença é que não precisamos possar
# a chave que queremos remover, ele vai removendo na sequência, e como nao informamos
# chave nenhuma, quando ele não encontrar mais, irá retornar um KeyError

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "Rogerio@gmail.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
}

print(contatos.popitem())

print(contatos.popitem())