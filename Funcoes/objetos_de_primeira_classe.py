# -------------------------------- INTRODUÇÃO ----------------------------------------
# Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos 
# de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como
# parâmetros para funções, usá-las como valores em estruturas de dados(listas, tuplas,
# dicionários, etc) e usar como valor de retorno para uma função (closures).

# --------------------------------- EXEMPLO -------------------------------------------

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def teste(a, b):
    return a*2 + b*4

def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é de = {resultado}")

exibir_resultado(10, 10, somar) # resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, teste) # 60


