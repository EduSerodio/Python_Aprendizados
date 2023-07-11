# ----------------------------------INTRODUÇÃO--------------------------------------
# Conjunto de python não suportam indexação e nem fatiamento, caso queira acessar os
# seus valores é necessário converter o conjunto para lista.

# ----------------------------------EXEMPLO------------------------------------------

numeros = {1, 2, 3, 2} # set

numeros = list( numeros) # conversão de set para list

print(numeros[0])