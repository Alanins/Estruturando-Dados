dicionario_padrao = {1:{"nome":"Maria", "idade":26, "nacionalidade":"brasileira"}}
novos_elementos = {"cidade":"recife", "estado":"pernambuco-PE"}

dicionario_padrao.update(novos_elementos) #atualizar o dicionário
dicionario_padrao2 = dicionario_padrao.copy() #copiar o dicionário
remover_dic_padrao = dicionario_padrao[1].pop("nacionalidade") #remover um elemento do dicionário
remove_item_dic_padrao = dicionario_padrao[1].popitem() #remover um item
#limpando_dicionario_padrao = dicionario_padrao.clear() #limpar o dicionário
#limpando_novo_dicionario = novo_dicionario.clear() #limpar o dicionário
novo_dicionario = dict.fromkeys(dicionario_padrao, dicionario_padrao2) #criar um novo dicionário utilizando dict.fromkeys

itens = novo_dicionario.items() #imprimir os itens
chaves = novo_dicionario.keys() #imprimir as chaves
valores = novo_dicionario.values() #imprimir os valores

# for itens in novo_dicionario.items():
#     print(itens)

# for chaves in dict.fromkeys(novo_dicionario):
#     print(chaves)

for valor in novo_dicionario[1].values():
    print(valor)

#print(novo_dicionario)