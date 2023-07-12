# -------------------------------- INTRODUÇÃO ----------------------------------------
# Para retornar um valor, utilizamos a palavra reservada RETURN. Toda função python
# retorna None por padrão. Diferente de outras linguagens de programação, em python uma
# função pode retornar mais de um valor.

# --------------------------------- EXEMPLO -------------------------------------------

#função que recebera uma lista de numeros e realizará a soma total
def calcular_total(numeros):
    return sum(numeros)

#função que vai receber um numero como parâmetro e retornar o antecessor e sucessor 
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    
    return antecessor, sucessor

#chamando e printando as funções criadas anteriormente
print(calcular_total([10, 20, 34]))

print(retorna_antecessor_e_sucessor(10))
#O retorno dessa função vai ser uma tupla, pois a tupla é um valor imutável