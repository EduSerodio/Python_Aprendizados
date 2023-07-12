# ---------------------------------INTRODUÇÃO----------------------------------------
# {}.FROMKEYS - Serve para adicionarmos chaves no dicionários, mas temos duas cituações
# de uso
# -----------------------------------Exemplos------------------------------------------

#PRIMEIRA
#CRIA as chaves com o valor 'nome'
print(dict.fromkeys(["nome", "telefone"]))

#SEGUNDA
#Cria as chaves com o valor vazio
print(dict.fromkeys(["nome", "telefone"], "vazio"))
