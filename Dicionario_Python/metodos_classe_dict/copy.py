# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.COPY - Método que cria uma cópia da chave de um dicionário mas com outros valores
# e quando usar?  Quando queremos manipular um dicionário mas sem alterar seus valores
# internos

# -----------------------------------Exemplos------------------------------------------
contatos = {
    "eduardo@gamil.com" : {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"},
}

copia = contatos.copy()
copia["eduardo@gamil.com"] = {"nome": "Edu"}

print(contatos)
print(copia)
