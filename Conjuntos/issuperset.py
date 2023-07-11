# ----------------------------------INTRODUÇÃO--------------------------------------
# {}.ISSUPERSERT -  Serve para verificarmos se os elementos estão dentro de outro 
# conjunto, assim retornando um valor booleano. MAS é o contrário de issubset

# ----------------------------------EXEMPLO------------------------------------------

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))