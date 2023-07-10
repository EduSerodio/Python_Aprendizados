# INTRODUÇÃO: Usamos para copiar os objetos de uma lista mas sem alterar de fato o id da lista

lista = [1, "python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)