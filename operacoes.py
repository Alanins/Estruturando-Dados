# Missão pátrica 
def calcular_media(notas):
    return sum(notas) / len(notas)
    

#Crie um método, que receberá o valor da média e retornará um
#booleano, para verificar se o aluno foi reprovado. Será considerado
#como reprovado um aluno com média inferior a 6;

def verificar_reprovado(media):
    if media < 6:
        return True
    else:
        return False
    
# Crie um método, que receberá dois parâmetros - os dados dos
# alunos e os números das matrículas dos alunos reprovados – e
# retornará a seguinte saída:
# ‘Aluno Reprovado: NOME DO ALUNO – Matrícula: MATRÍCULA
# DO ALUNO – Média Final: MÉDIA FINAL DO ALUNO’


def dados_dos_alunos(alunos, alunos_reprovados):
    for aluno in alunos:
        if aluno['media'] in alunos_reprovados:
            print(f"Aluno Reprovado: {aluno['nome']} - Matrícula: {aluno['matricula']} - Média Final: {aluno['media']}")
