# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.SETDEFAULT - Serve para adicionarmos um valor caso ele não exista dentro de 
# nossa lista, se ele existir nada vai acontecer e ele vai respeitar as informações
# já existentes

# -----------------------------------Exemplos------------------------------------------
contatos = {"nome": "Eduardo", "idade": 23, "telefone": "1234-5678"}

contatos.setdefault("nome", "Giovana")
print(contatos)

contatos.setdefault("tamanho", 175)
print(contatos)




