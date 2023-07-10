# -------------------------------- INTRODUÇÃO ----------------------------------
# A compreensão de lista oferece uma sintaxe mais curta quando você desejar:
# criar uma nova lista com base nos valores de uma lista existente(filtro) ou
# gerar uma nova lista aplicando alguma modificação nos elementos de uma lista
# existente.

# ---------------------------------- EXEMPLO -----------------------------------

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in  numeros:
    if numero % 2 == 0:
        print(pares.append(numero)) # o método .append() serve para adicionarmos valores a lista

# O python tem uma outra forma de realizar esse operação, que é por meio da compreesão

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

# podemos tambem realizar uma operação onde queremos deixar todos os itens da lista ao quadrado

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# ou

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]