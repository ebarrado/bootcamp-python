linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
#ordenar alfabeticamente
#Padrão

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
#Reverse ordena espelha

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
#lambda função anonima
#len tamanho da palavra

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
#com reverse menor ficara por ultimo



