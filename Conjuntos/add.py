# ----------------------------------INTRODUÇÃO--------------------------------------
# {}.ADD-  Serve para adicionar elementos a um set, quando o valor for existente
# dentro do set, se ele ja existir ele apenas ignora

# ----------------------------------EXEMPLO------------------------------------------

sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio)