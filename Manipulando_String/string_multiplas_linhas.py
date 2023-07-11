# ---------------------------------INTRODUÇÃO--------------------------------------------
# String de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante
# a atribuição. Elas podem ocupar várias linhas de código, e todos os espaços em branco
# são incluidos na string final.

# STRINGS TRIPLAS:
# ----------------------------------EXEMPLO----------------------------------------------

nome = "Guilherme"

mensagem = f"""
Olá meu nome é  {nome},
Eu estou aprendendo python
"""

print(mensagem)

# SAIDA: 
# Olá meu nome é Guilherme
# Eu estou aprendendo Python

mensagem = f'''
    Olá meu nome é  {nome},
  Eu estou aprendendo python
    Essa mensagem tem diferentes recuos.
'''
print(mensagem)

#SAIDA:
#   Olá meu nome é Guilherme,
#  Eu estou aprendendo python.
#     Essa mensagem tem diferentes recuos 

print('''
########## MENU #########

 1 - SACAR
 2 - DEPOSITAR
 3 - SAIR

#########################
 
- Obrigado por usar nosso sistema!!

''')