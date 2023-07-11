# ---------------------------------INTRODUÇÃO----------------------------------------
# São estruturas utilizadas para repetir um trecho de código um determinado número de
# vezes. Esse número pode ser conhecido previamente ou determinado através de uma 
# expressão lógica.
##

# EXEMPLO sem repetição:
# Receba um número do teclado e exiba os 2 números seguintes:

a = int(input("Informe um número inteiro: "))
print(a)
#

a += 1 
print(a)

a += 1 
print(a)

# "FOR" - O comando for é usado para percorrer um objeto iterável. Faz sentido usar
# "for" quando sabemos o número exato de vezes que nosso bloco de código deve ser
# executado, ou quando queremos percorrer um objeto iterável.

# ----------------------------------EXEMPLO------------------------------------------

texto = input("Informe um texto: ") 
VOGAIS = "AEIOU"  # variavel const que não poderá mudar seu valor no decorrer do código

for letra in texto:
    if letra.upper() in VOGAIS:  # .upper() serve para deixar a letra em maiúsculo
        print(letra, end="")
print()  # adiciona uma quebra de linha 

# FUNÇÃO RANGE - É uma função built-in do python, ela é usada para produzir uma 
# sequência de números inteiros a partir de um ínicio (inclusivo) para um fim
# (exclusivo). se usarmos range(i.j) será reproduzido:
#
# i, i+1, i+2, i+3, ...,j-1.
#
# Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step (opcional).

# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))

# utilizando o RANGE com o FOR:

for numero in range(0,11):
    print(numero, end=" ") # O end="" é para o resultado ser mostrado sempre um na frente do outro dando espaço em branco

print() # para gerar uma quebra de linha para o seguinte código 

# exibindo a tabuada do 5

for numero in range(0, 51, 5): # o valor "5" que foi colocado no final dos parâmetros, quer dizer que você
    print(numero, end=" ")      # está pedindo para o resultado vir de 5 em 5 : 0, 5, 10, 15 ...

print() # para gerar uma quebra de linha para o seguinte código 

# WHILE - É usado para repetir um bloco de código várias vezes. Faz sentido usar o WHILE
# quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo contrato...")


# EXEMPLO usando o BREAK:

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break   # Serve para quando a condição atendida ele corta o laço de repetição!

    print(numero)


# Podemos usar uma variação do break, chamado de CONTINUE:

for numero in range(100):

    if numero == 12:
        continue # Serve para pular o valor que escolhermos para nossa condição que no caso é 12

    print(numero, end=" ")