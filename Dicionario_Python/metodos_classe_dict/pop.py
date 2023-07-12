# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.POP - Usamos para remover uma chave do dicionário, um diferencial que podemos
# passar a chave que desejamos para ser removido, caso removido ele retorna a chave
# que foi removido, e caso nao encontrada, podemos reornar uma chave vazia

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "Rogerio@gmail.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
}

resultado = contatos.pop("Rogerio@gmail.com")
print(resultado)


resultado2 = contatos.pop("Rogerio@gmail.com", {})
print(resultado2)
