# -------------------------------- INTRODUÇÃO ----------------------------------------
# Por padrão, argumentos podem ser passados para uma função Python tanto por posição 
# quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz
# sentido restringit a maneira pelo qual argumentos possam ser passados, assim um
# desenvolvedor precisa apenas olhar para definição da função para determinar se os 
# itens são passados por posição, por posição e nome, ou por nome.

# --------------------------------- EXEMPLO -------------------------------------------

# POSITIONAL ONLY
#os 3 primeiros parâmetros não precisam ser parâmetros nomeados, ja o resto é obrigatório
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#chamando a função do jeito válido:
criar_carro("Polo", 2003, "abc-1234", marca="Volkswagem", motor="1.6", combustivel="gasolina")

#chamando a função do jeito inválido:
#criar_carro(modelo="Polo", ano=2003, placa="abc-1234", marca="Volkswagem", motor="1.6", combustivel="1.6")

# KEYWORD ONLYN
# todos os parâmetros da função terão que ser só por nome "parâmetros nomeados"
def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#forma válida de chamar a função:
criar_carro2(modelo="Polo", ano=2003, placa="abc-1234", marca="Volkswagem", motor="1.6", combustivel="gasolina")

#forma inválida de chamar a função:
#criar_carro2("Polo", 2003, "abc-1234", marca="Volkswagem", motor="1.6", combustivel="gasolina")

# KEYWORD AND POSITIONANDL ONLY "hibrido"
# onde estamos passando parâmetros que precisam ser passados apenas por posição antes da"/"
# e parâmetros que precisam ser por parâmetros nomeados "*"

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#chamando a função do jeito válido:
criar_carro3("Polo", 2003, "abc-1234", marca="Volkswagem", motor="1.6", combustivel="gasolina")

#forma inválida de chamar a função:
#criar_carro3(modelo="Polo", ano=2003, placa="abc-1234", marca="Volkswagem", motor="1.6", combustivel="gasolina")

