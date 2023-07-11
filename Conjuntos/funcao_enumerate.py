# ----------------------------------INTRODUÇÃO--------------------------------------
# Ás vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso
# podemos usar a função enumerate

# ----------------------------------EXEMPLO------------------------------------------

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")