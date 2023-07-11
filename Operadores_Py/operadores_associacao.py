# INTRODUÇÃO: São operadores ultilizados para verificar se um objeto está presente em uma sequência

curso = "Curso de python" #variavel curso que recebe uma string que também é uma sequencia de caracteres
frutas = ["laranjas", "uvas", "limao"] #variavel frutas que recebe uma lista de frutas
saques = [1500, 100] #variavel saques, que recebe uma lista de numero inteiros

print("python" in curso)
print("maça" not in frutas)
print(200 in saques)

# ele esta verificando se dentro das sequências existe ou não o objeto selecionado

# Mais exemplos práticos :

frutas = ["limao", "uva"] #variavel frutas recebendo uma lista de frutas
curso = "curso de programacao python" #variavel curso, recebendo uma string que é uma sequencia de caracteres portanto pode receber a associacao

print("laranja" in frutas) # verificando se há laranja na lista de frutas com o operador "in"
print("limao" not in frutas) # verificacao se nao há limao na lista de frutas, com o operador "not in"
print("programacao" in curso) # verificacao se há a palavra "programacao" dentro da variavel curso, com o operador "in"