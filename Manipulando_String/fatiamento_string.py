# ---------------------------------INTRODUÇÃO--------------------------------------------
# Fatiamento de Strigs é uma técnica utilizada para retornar substrings (partes da string  
# original), informando inicio (start), fim(stop) e passo (step): [start: stop[, step]].

# FATIAMENTO
# ----------------------------------EXEMPLO----------------------------------------------

nome = "Guilherme Arthur de Carvalho"

nome[0]
# retorna: "G"
nome[:9]
# retorna: "Guilherme"
nome[10:]
# retorna: "Arthur de Carvalho"
nome[10:16]
# retorna: "Arthur"
nome[10:16:2]
# retorna:"Atu"
nome[:]
# retorna: "Guilherme Arthur de Carvalho"
nome[:: -1]
# retorna: "ohlavrac ed ruhtra emrehliuG"