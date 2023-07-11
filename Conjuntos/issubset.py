# ----------------------------------INTRODUÇÃO--------------------------------------
# {}.ISSUBSET -  Serve para verificarmos se os elementos estão dentro de outro 
# conjunto, assim retornando um valor booleano.

# ----------------------------------EXEMPLO------------------------------------------

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))