# Exemplo de variaveis em PYTHON:

age = 23
name = "Eduardo"
print(f"a idade do {name} é de {age} anos!") #OBS: Para realizar uma concatenação na hora de exibir uma mensagem em python usamos o "f" dentro dos parenteses e "{}" para chamar a variavel

# Para substituirmos os valores das variaveis escrita a cima, é só passarmos outros valores com o mesmo nome dado a eles:

age = 45
name = "Gabriel"
print(f"a idade do {name} é de {age} anos!")

# E se quisermos deixar um valor fixo vamos usar uma variavel constante, mas para definir que essa variavel é uma constante vamos usar a "convenção" deixando o nome da variável em letra maiúscula.

# Exemplos:

ABS_PATH = '/home/guilherme/documents/python_course' # aqui eu defino que meu projeto sempre vai começar com essa caminho das pastas

DEBUG = True # Aqui eu declaro que se meu código começou com o debug, ele vai ter que permanecer até o fim

STATES = [
    'SP',
    'RJ',   # Aqui definimos uma lista de estados que nao podera mudar durante o resto do código
    'MG',
]
 
AMOUNT = 30.5 # Aqui definimos um valor que nao pode mudar 

#---------------------------- BOA PRÁTICAS ----------------------------

# - o padrão de nomes deve ser em snake case: projetos_python.
# - Escolher nomes sugestivos.
# - Nome de constantes todo em maiúsculo.
