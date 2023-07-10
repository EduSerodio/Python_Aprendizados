# -------------------------------- INTRODUÇÃO ----------------------------------
# Ás vezes é necessário saber qual o índice do objeto dentro do lalo for. Para 
# isso podemos usar a função enumerate

# ---------------------------------- EXEMPLO -----------------------------------

carros = ["gol", "polo", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")