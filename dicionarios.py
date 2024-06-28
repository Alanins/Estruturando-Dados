#Microatividade 4: Descrever a criação da estrutura de dados dicionário em Python


meu_dicionario = {"codigo = 1": "linguagem = python", 
                  "codigo = 2": "linguagem = java", 
                  "codigo = 3": "linguagem = PHP"}

dicionario_frutas = {"chave:1" :"valor:{nome = limão, tipo = ácida}",
                     "chave:2" :"valor:{nome = laranja, tipo = ácida }",
                     "chave:3" :"valor:{nome = manga, tipo = semiácida }",
                     "chave:4" :"valor:{nome = maçã, tipo = semiácida}",
                     "chave:5" :"valor:{nome = banana, tipo = doce }",
                     "chave:6" :"valor:{nome = mamão, tipo = doce }"}
                     
tamanho = len(meu_dicionario)

linguagem = meu_dicionario.get("codigo = 3")
chave = dicionario_frutas.get("chave:2") 
valores = dicionario_frutas.values()

for valores in dicionario_frutas.values():
    print(valores)

