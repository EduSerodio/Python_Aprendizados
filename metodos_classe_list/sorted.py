# INTRODUÇÃO: Serve também para ordenar objetos iteráveis

linguagens = ["python", "java", "c#", "c", "javascript"]
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))