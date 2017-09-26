#Minimo de 50 creditos para poder colar grau
#disciplina = 2 creditos
#atividade_complementar = 1 credito
#funcao chamada pode_formar: recebe numero de disciplinas cursadas
# e a quantidade de atividades complementares realizadas.
# a função deve retornar se o aluno está apto a se formar ou não

def pode_formar(qtd_disciplinas_cursadas, qtd_atividades_realizadas):
	total_creditos = (qtd_disciplinas_cursadas*2)+qtd_atividades_realizadas

	if total_creditos >= 50:
		return "Apto a se formar"
	else:
		return "Não está apto a se formar"

print("Sistema que verifica se aluno está apto a se formar")
qtd_disciplinas_cursadas = int(input("Quantas disciplinas foram cursadas? "))
qtd_atividades_realizadas = int(input("Quantas atividades foram realizadas? "))

print(pode_formar(qtd_disciplinas_cursadas, qtd_atividades_realizadas))
