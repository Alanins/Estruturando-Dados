from operacoes import calcular_media, verificar_reprovado, dados_dos_alunos

#Crie as estruturas de dados necessárias para armazenar os dados
#dos alunos e as notas
dados_alunos = [
  {"nome": "Maria", "matricula": "26", "notas": [8, 7, 5, 9]},
  {"nome": "Ana", "matricula": "101","notas": [9, 9, 8, 9]},
  {"nome": "João", "matricula": "13", "notas": [6, 5, 5, 5]},
  {"nome": "Ágatha", "matricula": "37", "notas": [8, 6, 7.5, 9]},
  {"nome": "Joaquim", "matricula": "72","notas": [6, 5.5, 5, 7]},
  {"nome": "Félix","matricula": "5", "notas": [10, 8, 8, 8]}
]


#calcular a média de cada aluno

for aluno in dados_alunos:
    media = calcular_media(aluno['notas'])
    aluno['media'] = media 
    print(f"Aluno: {aluno['nome']} - Matrícula: {aluno['matricula']} - Média Final: {aluno['media']}")

#verificar se o aluno foi reprovado;
for aluno in dados_alunos:
    reprovado = verificar_reprovado(aluno['media'])
    print(verificar_reprovado(aluno['media']))    

#identificar qual aluno foi reprovado;
for aluno in dados_alunos:
    if verificar_reprovado(aluno['media']):
     print(dados_dos_alunos(dados_alunos, [aluno['media']]))