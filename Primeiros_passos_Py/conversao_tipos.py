# INTRODUÇÃO: Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente.
# EXEMPLO:  Variáveis do tipo String, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

# Se precisarmos converter um número inteiro para float seria da seguinte forma:


preco = 10     #numero inteiro 
print(preco)   #retornaria 10

preco = float(preco) #Aqui fazemos a conversao para float
print(preco)         #retornaria 10.0

#Podemos fazer essa conversão ao contrário também:

preco = 10.0  #numero do tipo float
print(preco)  #retornaria 10.0

preco = int(preco) #Aqui fazemos a conversão de float para inteiro
print(preco)       #retornaria 10

# Agora para converter numérico para string 

preco = 10.50
idade = 25

print(str(preco))  #Aqui o valor de preço que seria float passa a ser uma string

print(str(idade))  #Aqui o valor int da idade passsa a ser string

texto = f"idade {idade} preco {preco}" #Aqui novamente vemos a concatenação para retornar em uma mensagem

print(texto)


# Podemos também realizar a conversão de String para números (que é bastante usado hoje em dia) EXEMPLO:
preco = "25.16"
idade = 65

print(float(preco)) #Aqui convertemos a string para tipo numérico float

print(int(idade)) #Aqui convertemos a string para tipo numérico int


# Podemos usar para facilitar o entendimento do código "TYPE" que nos mostra qual é p tipo de dado que esta sendo usado. EXEMPLO:

valor = 35
valor_convertido_string = str(valor)

print(type(valor))  #Aqui ele retonrará no terminal o seguinte <class 'int'>

print(type(valor_convertido_string))  #Aqui ele retornará no terminal <class 'str'>

# Na divisão podemos observar o seguinte:

print(100 / 2)  # Nesse caso usando uma vez o operador "/" ele retonará 52.0 do tipo float

print(100 // 2)  # Já nesse caso se usarmos duas vezes o operador "//" ele retorna o valor como inteiro 50

