# ---------------------------------INTRODUÇÃO--------------------------------------------
# Em python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal
# de "%", a segunda é utilizando o método "format" e a última é utilizando "f" strings.
# A primeira forma não é atualmente recomendada e seu uso em python 3 é raro, por esse
# motivo iremos focar nas 2 ultimas:

# OLD STYLE "%" (Não é recomendado usar nos dias atuais)
# ----------------------------------EXEMPLO----------------------------------------------

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s " 
    % (nome, idade, profissao, linguagem))
 # A saída será: Ola, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Programador e estou
 # matriculado no curso de Python

# MÉTODO FORMAT
# ----------------------------------EXEMPLO----------------------------------------------

nome = "Eduardo"
idade = 23
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." 
    . format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." 
    . format(linguagem, profissao, idade, nome))

# F-STRING
# ----------------------------------EXEMPLO----------------------------------------------

nome = "Eduardo"
idade = 23
profissao = "Progamador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")

# FORMATAR STRING COM F-STRING
# ----------------------------------EXEMPLO----------------------------------------------

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # o .2 pega somente os dois valores depois da virgula que está na string
# A saída será: "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}") # a formatação 10.2f vai ter 10 espaços antes do resultado e os dois valores após a virgula
# A saída será: "Valor de PI:          3.14"


