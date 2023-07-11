# -----------------------------------INTRODUÇÃO---------------------------------------
# É uma forma de manter o código fonte mais legível e manutenível. Mas em python,
# ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde 
# um bloco de comando inica e onde ele termina.
#

# Existe uma convenção em python, que define as boas práticas para escrita de código na linguagem.
# Nesse documento é indicado ultilizar 4 espaços em branco por nível de identação, ou seja,
# a cada novo bloco adicionamos 4 novos espaços em branco.


# -----------------------------------Exemplos------------------------------------------

def sacar(valor):  # início do bloco do método
    saldo = 500

    if saldo >= valor:  # início do bloco do IF
        print("Saque efetuado com sucesso!")

    # fim do bloco do IF

# fim do bloco do método    
sacar(100)