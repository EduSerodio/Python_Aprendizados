# INTRODUÇÃO: Serve para ordenar nossa lista.

linguagens = ["python", "java", "c#", "c", "javascript"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "java", "c#", "c", "javascript"]
linguagens.sort(reverse=True) # vai ordenar no sentido contrário
print(linguagens)

linguagens = ["python", "java", "c#", "c", "javascript"]
linguagens.sort(key=lambda x: len(x)) # vai ordenar da menor para maior 
print(linguagens)

linguagens = ["python", "java", "c#", "c", "javascript"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ordena da maior para menor no sentido contrário 
print(linguagens)