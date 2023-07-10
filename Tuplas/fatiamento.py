# ------------------------------------- INTRODUÇÃO --------------------------------------
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma 
# sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto
# Podemos ainda informar quantas posições o cursor deve "pular" no acesso

# -------------------------------------- EXEMPLO ----------------------------------------

lista = ["p", "y", "t", "h", "o", "n",]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] #["n", "o", "h", "t", "y", "p"]