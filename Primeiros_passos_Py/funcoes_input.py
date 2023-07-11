# INTRODUÇÃO Input: a função builtin input é ultilizada quando queremos ler dados de entrada padrão (teclado).
# Ela recebe um argumento do tipo STRING, que é exibido para o usuário na saída padrão (TELA). A função lê a entrada,
# converte para STRING e retorna o valor. 

# EXEMPLO:

nome = input("Informe seu nome: ")

idade = input("Informe sua idade: ")


# INTRODUÇÃO função print: A função builtin print é ultilizada quando queremos exibir dados na saída padrão (tela). Ela recebe
# um argumento obrigatório do tipo varags de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são 
# convertidos para string, separados por sep e terminaod spor end. A string final é exibida para o usuário.

# EXEMPLO:

nome = "Eduardo"
sobrenome = "Serodio"

print(nome, sobrenome) #Aqui on retorno será = Eduardo Serodio
print(nome, sobrenome, end="...\n") #Aqui o retorno será Eduardo Serodio... e como usamos o parâmetro "end="...\n"" ele vai ter uma quebra de linha 
print(nome, sobrenome, sep="#")  #Aqui o retorno seŕa Eduardo#Serodio, como usamos o parâmetro sep="#" ele seria um separador mas usamos um caracter para separar os nomes


