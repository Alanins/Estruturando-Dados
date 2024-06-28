#Microatividade 3: Descrever a manipulação da estrutura de dados set em Python

set_inicial = {11, 12, 13, 14}
novo_set = {20, 21, 23, 1, 2}

set_inicial.add(15)
set_inicial.update([1,2,3,4,5])
set_inicial.discard(13)

uniao_sets = set_inicial.union(novo_set)

inter = set.intersection(set_inicial, novo_set)
diferenca = set.difference(set_inicial, novo_set)
dif_simetrica = set.symmetric_difference(set_inicial, novo_set)

print(uniao_sets,dif_simetrica)
