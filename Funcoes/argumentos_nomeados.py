# -------------------------------- INTRODUÇÃO ----------------------------------------
# Funções também podem ser chamadas usando argumentos nomeados de forma chave=valor

# --------------------------------- EXEMPLO -------------------------------------------

#Função criada para salvar carro no banco de dados...
def salvar_carros(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#3 métodos de chamarmos essas funções:

#1º-
salvar_carros("Volkswagem", "Polo", 2003, "ABC-1234")

#2º-
salvar_carros(marca="Volkswagem", modelo="Polo", ano=2003, placa="abc-1234")

#3º-
salvar_carros(**{"marca": "Volkswagem", "modelo": "Polo", "ano": 2003, "placa": "abc-1234"})

# Por segurança o jeito mais seguro e apropriado de se chamar uma função é o 2º
# com argumentos nomeados, pois não corre o risco de alguem inverter os valores
# e acabar acontecendo algum erro durante o resto do código.

# o 3º jeito ele armazena os valores em forma de dicionário.