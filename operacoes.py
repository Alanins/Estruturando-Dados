#Missão Prática

#Calculo da média;
def calcular_media(notas):
    return sum(notas) / len(notas)
#Recebe o valor da média e retornar um booleano, verificando se o aluno foi reprovado;
def verificar_reprovado(media):
    if media < 6:
        return True
    else:
        return False
# Recebe dois parâmetros - os dados dos alunos e as matrículas dos alunos reprovados;
def dados_dos_alunos(alunos, alunos_reprovados):
    for aluno in alunos:
        if aluno["media"] in alunos_reprovados:
            print(f"Aluno Reprovado: {aluno["nome"]} - Matrícula: {aluno["matricula"]} - Média Final: {aluno["media"]}")
