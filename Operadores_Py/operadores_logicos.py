# INTRODUÇÃO: São operadores ultilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.
# Quando um operador de comparação é ultilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores,
# de comparação com os operadores lógicos, exemplo:

# op_comparacao + op_logico + op_comparacao...N...

# EXEMPLO 

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)  # Retorna um booleano "True"

print(saque <= limite)  # Retorna um booleano "False"

#OPERADOR E (AND)


saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite) # Para retornar um valor booleano "True" as duas condições precisam ser verdadeiras se uma não atender ele retorna "false"

#OPERADOR OU (OR)


saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite) # Para retornar um valor booleano "True" uma condição pelo menos tem que ser verdadeira.


# OPERADOR NEGAÇÃO (NOT)

# contatos_emergencia 

# not 1000 > 1500 - Aqui retornaria "false" mas como usamos o operador not, o retorno dessa operação é "true"

# not contatos_emergencia  - Aqui retornaria "false" mas como usamos o operador not, o retorno será "true"

# not "saque 1500;" - AQui o retorno seria "true", mas como usamos o operador not, o retorno será "false"

# not "" - Aqui o retorno seria "false", mas como usamos o operador nor, o retorno será "true"


# PARÊNTESES 

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print( saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

# as duas expressões acima são válidas e atendem a regra de negócio, mas a segunda entra melhor como boas práticas

# Sempre é bom evitar construir uma expressão muito longa, pois assim fica muito dificil compreender, para isso podemos
# dividir as expressões em duas variaveis:

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp)
