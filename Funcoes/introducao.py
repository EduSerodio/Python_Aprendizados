# -------------------------------- INTRODUÇÃO ----------------------------------------
# Função é um bloco de código identificado por um nome e pode receber uma lista de 
# parâmetros, esses parâmetros podem não ter valores padrões. Usar funções torna 
# o código mais legível e possibilita o reaproveitamento de código. Programar baseado
# em funções, é o mesmo que dizer que estamos programando de maneira estruturada.
#  E para isso usamos a palavra reservada para função = def.

# --------------------------------- EXEMPLO -------------------------------------------

#Criando uma função sem parâmetros 
def exibir_mensagem():
    print("Ola mundo")

#Criando uma função com o parâmetro nome
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

#Criando uma função com parâmetro nome ja definido, mas pode ser alterado na chamada dessa função
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2("Eduardo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")