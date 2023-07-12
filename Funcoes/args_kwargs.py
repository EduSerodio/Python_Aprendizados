# -------------------------------- INTRODUÇÃO ----------------------------------------
# Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos
# (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

# --------------------------------- EXEMPLO -------------------------------------------

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de Agosto de 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than  implict.",
    "Complex is better than comclicated.",
    "Flat is better than nested",
    "Sparse is better than dense.",
    "Readability counts.",
    autor="Tim Peters",
    ano=1999,


)