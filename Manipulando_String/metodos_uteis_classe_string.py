# ---------------------------------INTRODUÇÃO--------------------------------------------
# Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores 
# de variáveis e entender como funciona o fatiamento.
# A classe String do python é famosa por ser rica em métodos e possuir uma interface muito 
# fácil de trabalhar. Em algumas linguagens, manipular sequências de caracteres não é um 
# trabalho trivial, porém, em python esse trabalho é muito simples.

# manipulando para, Maiúscula, minúscula e título:
# ----------------------------------EXEMPLO----------------------------------------------

curso = "pYtHon"

print(curso.upper()) # o método ".upper()" vai converter todos os caractéres para MAIÚSCULO
# a saída será: PYTHON
print(curso.lower()) # o método ".lower()" vai converter todos os caractéres para minúsculo
# a saída será: python
print(curso.title()) # o método ".title()" vai converter o primeiro caractér para Maiúsculo e o resto fica minúsculo
# a saída será: Python

# Eliminando espaços em branco:
# ----------------------------------EXEMPLO-----------------------------------------------

curso = "   Python "

print(curso.strip()) # o método ".strip()" vai retirar todos os espaços dentro da sting tanto do lado esquerdo como do lado direito
# a saída será: "Python"
print(curso.lstrip()) # o método ".lstrip()" vai retirar todos os espaços da esquerda de dentro da sting
# a saída será: "Python  "
print(curso.rstrip()) # o método ".rstrip()" vai retirar todos os espaços da direita  de dentro da sting
# a saída será: "  python"

# Junções e Centraliozação
# ----------------------------------EXEMPLO-----------------------------------------------

curso = "Python"

print(curso.center(10, "#")) # o método ".center(10, "#")" recebe dois argumentos: "10" é referente
# a quantidade de caracteres que eu quero ter em minha string, e o "#" serve para preencher os
# espaços que vão sobrar nas laterais, segue o exemplo abaixo:
# a saída será: "##Python##"
print(".".join(curso)) # o método de junção vai receber o caractér antes e o método em seguida
# ficando assim "."".join", então ele vai percorrer letra por letra da variavel curso, e colocar
# o caractér que ele esta recebendo, segue o exemplo abaixo:
# a saída será: "P.y.t.h.o.n"

