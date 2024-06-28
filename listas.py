#Microatividade 1: Descrever a manipulação da estrutura de dados lista em Python

lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
lista_mesclada.append("Lista aninhada")
lista_mesclada.insert(4,5)

lista_mesclada.pop(1)

nova_lista_mesclada = []
for i in range(5):
    nova_lista_mesclada.append(lista_mesclada[i])

tamanho = len(nova_lista_mesclada)
print(nova_lista_mesclada, tamanho)