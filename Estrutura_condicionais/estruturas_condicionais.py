# ---------------------------------INTRODUÇÃO----------------------------------------
# A estrutura condicional perminte o desvio de fluxo de controle, quando determinadas
# expressões são atendidas.
#

# "IF" - Para criar uma estrutura condicional simples, composta por um único desvio,
# podemos ultilizar a palavra reservada "IF". O comando irá testar a expressão lógica,
# e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão 
# executadas.

# ----------------------------------EXEMPLO------------------------------------------

saldo = 1000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    saldo_atual = saldo - saque
    print(f"Saque efetudo com sucesso! seu saldo atual é de: {saldo_atual} ")

if saldo < saque:
    print("Saldo insuficiente!")    


# "IF/ELSE" - Para criar uma estrutura condicional com dois desvios, podemos ultilizar
# as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if
# for verdadeira, então o bloco de código do if será executado. caso contrário o bloco
# else será executado.

# ----------------------------------EXEMPLO------------------------------------------

saldo =  5000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    saldo_atual = saldo - saque
    print(f"Saque efetudo com sucesso! seu saldo atual é de: {saldo_atual} ")
else:
    print("Saldo insuficiente!")

# "IF/ELIF/ELSE - Em alguns cenários queremos mais de dois desvios, para isso podemos
# ultilizar a palavra reservada "elif". O elif é composto por uma nova expressão lógica,
# que será testada e caso retorne verdadeiro o bloco de código do elif será executado.
# Não existe um número máximo de elifs que podemos ultilizar, porém evite criar grandes
# estruturas de condicionais, pois elas aumentam a complexidade do código.

# ----------------------------------EXEMPLO------------------------------------------

opcao = int(input("Informe uma opção: [1] Sacar ou [2] Extrato: "))
saldo = 3000.0

if opcao == 1:
    saque = float(input("Digite o valor que deseja sacar: "))
    saldo_final = saldo - saque
    print(f"Saque efetuado com sucesso! \nAgora seu saldo atual é de: {saldo_final}")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")

# "IF - Aninhado" - Podemos criar estruturas condicionais aninhadas, para isso basta
# adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

# ----------------------------------EXEMPLO------------------------------------------
conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!")

# "IF - ternário" - Permite escrever uma condição em uma única linha. Ele é composto
# por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro,
# a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão
# não seja atendida.

# ----------------------------------EXEMPLO------------------------------------------

saldo = 1000
saque = 500
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
